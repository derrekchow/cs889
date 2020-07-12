$(function () {
    var w1 = null;
    var w2 = null;

    var isW1 = true;

    $('#w1').focus(() => {
        $('#w1').val('');
        $('#w1').removeClass('selected');
        $('#w1').width(50);
        isW1 = true;
    })
    $('#w1').on('input', (e) => {
        $('#w1').width($('#w1').val().length*15);
    })

    $('#w2').focus(() => {
        $('#w2').val('');
        $('#w2').removeClass('selected');
        $('#w2').width(50);
        isW1 = false
    })
    $('#w2').on('input', (e) => {
        $('#w2').width($('#w2').val().length*15);
    })

    console.log(data.slice(0, 100))
    $('.word').autocompleter({
        highlightMatches: true,
        source: data,
        template: '{{ label }} <span>({{ type }})</span>',
        empty: false,
        limit: 50,
        callback: function (value, index, selected) {
            if (selected) {
                if (isW1) {
                    w1 = selected;
                    $('#w1').addClass('selected');
                    $('#w1').width(selected.label.length*15);
                }
                else {
                    w2 = selected;
                    $('#w2').addClass('selected');
                    $('#w2').width(selected.label.length*15);
                }
            }
        }
    });
    $('#submit').click((function(e) {
        e.preventDefault();
        if (w1 != null && w2 != null) {
            var data = {
                'w1' : w1.code,
                'w2' : w2.code
            };
            $.ajax({
                type: 'GET',
                url: window.location.href,
                data: data,
                success: function(data) {
                    $('#ans').empty()
                    $('#ans-container').show()
                    $('#w1-ans').html(w1.label)
                    $('#w2-ans').html(w2.label)
                    for (word of data) {
                        $('#ans').append("<li>" + word + "</li>")
                    }
                }
            });
        }
    }))
});