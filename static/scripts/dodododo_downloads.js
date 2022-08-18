console.log("Loading Dodododo_downloads script");



/*

These event handlers allow the buttons to download the appropriate files 
by redirecting the page to the appropriate links. 

*/
document.getElementById("season1-btn").addEventListener("click", function() {
    console.log("season1-btn clicked");
    window.location.href = "./doodododo_download_skjafdkahesf";
});


document.getElementById("disastersmp-btn").addEventListener("click", function() {
    console.log("disastersmp-btn clicked");
    window.location.href = "./doodododo_download_disasterSMP";
});

document.getElementById("origins-btn").addEventListener("click", function() {
    console.log("origins-btn clicked");
    window.location.href = "./doodododo_download_season_2-origins";
});

document.getElementById("amplified-btn").addEventListener("click", function() {
    console.log("amplified-btn clicked");
    window.location.href = "./doodododo_download_StillNotAmplified";
});