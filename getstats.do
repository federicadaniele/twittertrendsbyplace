clear
set more off
* Set your directory here!
cd "/Users/federicadaniele/Downloads/pricescraping/"
********************************************************************************
* Import excel file containing Where On Earth Yahoo ID, latitude, longitude ****
import excel using woeidpop.xlsx, clear firstrow
save woeid.dta, replace

* Merge with Twitter data on trends (original 31 cities):
forv x = 1(1)31{
qui: import delimited using data`x'.csv, clear
qui: gen id = `x'
qui: gen ranking = _n
qui: ren v1 category
qui: ren v2 volume				/* this is aggregate volume */
qui: destring volume, force replace
merge m:1 id using woeid.dta
qui: drop if _merge!=3
qui: drop _merge
if `x'==1{
qui: save hashtags.dta, replace
}
else{
qui: append using hashtags.dta
qui: save hashtags.dta, replace
}
}

* retain trends, drop pages, people, mentions, etc:
qui: split category, parse("#")
qui: keep if category1 == ""
* needed to take care of same trends upper/lower case:
qui: gen catnew = upper(category2)
qui: drop category*
qui: ren catnew category
qui: drop if population == .
qui: drop if category == ""
qui: sort id ranking
qui: by id, sort: gen ranking_new =_n
qui: drop ranking
qui: ren ranking_new ranking
qui: egen catid = group(category)

preserve
qui: keep catid category
qui: duplicates drop
qui: save categoryid.dta, replace
restore

qui: ren id geoid

preserve
qui: keep geoid woeid city latitude longitude population share
qui: duplicates drop
qui: save geoid.dta, replace
restore

qui: keep geoid catid ranking
qui: duplicates drop
qui: reshape wide ranking, i(geoid) j(catid)
qui: reshape long ranking, i(geoid) j(catid)

* Balanced panel of categories and cities:
qui: merge m:1 geoid using geoid.dta
qui: drop _merge
qui: merge m:1 catid using categoryid.dta
qui: drop _merge

* Assign arbitrary score when not featured:
qui: replace ranking = 51 if ranking==.	
/* Measure of popularity ******************************************************/

preserve
* total share of population in locations where it is featured:
qui: gen absent = 1
qui: replace absent = 0 if ranking == 51
qui: by category, sort: egen totshare = total(share*absent)
* total number of locations where it is featured:
qui: by category, sort: egen count = total(absent)
* average counter (including locations where not featured):
qui: by category, sort: egen avgranking = mean(ranking)
* weighted average of ranking: trends with highest ranking especially in large city receive largest score:
qui: by category, sort: egen wgtranking = total(ranking*share)
qui: keep category catid wgtranking avgranking totshare count
qui: duplicates drop
qui: sort wgtranking
qui: global trending = category[1]
di "$trending"
restore
********************************************************************************
qui: egen idcity = group(city)
qui: sum idcity, detail
qui: global ncities = `r(max)'

* Index of disagreement:
qui: by category, sort: egen avgranking = mean(ranking)
qui: gen devsqrt = (ranking - avgranking)^2
qui: by city, sort: egen totdev = total(devsqrt)
qui: replace totdev = totdev/$ncities

qui: keep if category == "$trending"
qui: gen logpop = ln(population)
qui: gen logdev = ln(totdev)
qui: keep woeid logpop latitude longitude ranking logdev 
export delimited using finalplot22112017.csv, replace novarnames





