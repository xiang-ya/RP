$(document).ready(function () {
    // Defining the local dataset
    var school_list = ['Northeastern Univers', '河北传媒大学', '吉林大学', '广州农工']
    // Constructing the suggestion engine
    var school_list = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: school_list
    });

    // Initializing the typeahead
    $('.school').typeahead({
            hint: true,
            highlight: true, /* Enable substring highlighting */
            minLength: 1 /* Specify minimum characters required for showing result */
        },
        {
            name: 'school_list',
            source: school_list
        });
});

$(document).ready(function () {
    // Defining the local dataset
    var student_list = ['丁力']
    // Constructing the suggestion engine
    var student_list = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: student_list
    });

    // Initializing the typeahead
    $('.prof').typeahead({
            hint: true,
            highlight: true, /* Enable substring highlighting */
            minLength: 1 /* Specify minimum characters required for showing result */
        },
        {
            name: 'student_list',
            source: student_list
        });
});
