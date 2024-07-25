// This is the JS for the habit tracker.

console.log("hello world!")

let currentUser;

function drawHabits(){
    console.log("Current user: ", currentUser);

    // Clear away the "who are you" prompt
    $("main").empty();

    // Add logout button & logic
    $('<button class="logout" id="logout"> Log out </button>').appendTo("header");
    $("#logout").click(function(){
        // Simply redirect to empty site
        window.location.href = "/habits";
    });




    // Unpack data
    let habit_data = RAW_DATA['habitData'];
    let dad_score = RAW_DATA['dadScore'];
    let mom_score = RAW_DATA['momScore'];
    let total_score = RAW_DATA['totalScore'];


    // Display the current scores
    let scoreSection = $("<section class='habitTile'> </section>").appendTo("main");
    $("<h1> Combined score is " + total_score + "</h1>").appendTo(scoreSection);
    $("<p> Mom has a score of " + mom_score + "</p>").appendTo(scoreSection);
    $("<p> Dad has a score of " + dad_score + "</p>").appendTo(scoreSection);

    // Add a break
    $("<br><br><br><br>").appendTo("main");

    // For each habit, create the good bit
    for (let habit of habit_data ){

        let thisSection = $("<section class='habitTile'> </section>").appendTo("main");
        
        
        // Show current data for this habit
        $("<h2> " + habit.habitName + "</h2>").appendTo(thisSection);
        $("<h3> Combined score is " + habit.total + "</h3>").appendTo(thisSection);
        $("<p> Mom has a score of " + habit.MOM + "</p>").appendTo(thisSection);
        $("<p> Dad has a score of " + habit.DAD + "</p>").appendTo(thisSection);

        // Check if the index is -1 | this indicates that it is a dynamic point habit
        if (habit.pointValue == "-1"){

            // Add input box and submit btn
            let inputDiv = $("<div class='HorizontallyCenterItems'> </div>").appendTo(thisSection);

            let input = $("<input type='number' class='habitInput'> </input>").appendTo(inputDiv);
            let submitBtn = $("<button class='addBtn habitBtn'> + </button>").appendTo(inputDiv);
            let removeBtn = $("<button class='removeBtn habitBtn'> - </button>").appendTo(inputDiv);

            
            // Generate baseurl
            let baseurl = "/habits?";
            baseurl += "habitIndex=" + habit.index + "&";
            baseurl += "individual=" + currentUser + "&";

            submitBtn.click(function(){
                // Get custom value 
                let customValue = parseInt(input[0].value, 10);

                // append operation & redirect
                let url = baseurl + "operation=add&";
                url += "customValue=" + customValue + "&";
                window.location.href = url;

            });

            removeBtn.click(function(){
                // Get custom value 
                let customValue = parseInt(input[0].value, 10);

                // append operation & redirect
                let url = baseurl + "operation=sub&";
                url += "customValue=" + customValue + "&";
                window.location.href = url;
            });


        } else {
            // Add buttons
            let thisButtonDiv = $("<div class='HorizontallyCenterItems'> </div>").appendTo(thisSection);
            let addBtn = $("<button class='addBtn habitBtn'> +" + habit.pointValue + " </button>").appendTo(thisButtonDiv);
            let removeBtn = $("<button class='removeBtn habitBtn'> -" + habit.pointValue + "</button>").appendTo(thisButtonDiv);

            // Generate baseurl
            let baseurl = "/habits?";
            baseurl += "habitIndex=" + habit.index + "&";
            baseurl += "individual=" + currentUser + "&";

            // Add points when addBtn is clicked
            addBtn.click(function(){
                // append operation & redirect
                let url = baseurl + "operation=add";
                window.location.href = url;

            })

            removeBtn.click(function(){
                // append operation & redirect
                let url = baseurl + "operation=sub";
                window.location.href = url;
            });
        }
        

    }
}

$(document).ready(function(){    

    // Check if changes were made.
    if (RAW_DATA['madeChanges'] == true){
        // Changes made. Thus, remove all GET parameters from URL and reload.
        // This ensures that the user can reload the page
        // without re-modifying data (reloading would otherwise re-send the 
        // GET payload)
        window.location.href = "/habits?individual=" + RAW_DATA['user'];
    } else {
        // Check if user was specified in RAW DATA
        if (RAW_DATA['user']){

            // User is already logged in, so just run it
            currentUser = RAW_DATA['user']
            drawHabits();

        } else {
            $("#momUsingBtn").click(function(){
                currentUser = "MOM";
                drawHabits();
            });

            $("#dadUsingBtn").click(function(){
                currentUser = "DAD";
                drawHabits();
            });
        }
    }

});