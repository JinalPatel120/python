$(document).ready(function() {
   
    var $paragraph = $('#myParagraph');

    // Step 2: Change the text content of the selected element
    $paragraph.text('This is the new text content!');

    // Step 3: Add a CSS class to modify its appearance
    $paragraph.addClass('highlight');

    // Step 4: Attach a click event listener to the button
    $('#myButton').on('click', function() {
        // Step 5: Toggle the visibility of another element on click
        $('#hiddenDiv').toggle(500); // Animate the toggle with a duration of 500 milliseconds
    });
});
