var stepsopen=false;

function slideOpen()
{
	$('.steps').addClass('steps-open');	
	$('#arrow').addClass('arrow-rotated');
	stepsopen=true;
}

function slideClose()
{
	$('.steps').removeClass('steps-open');	
	$('#arrow').removeClass('arrow-rotated');
	stepsopen=false;
}

function slideToggle()
{
	if(stepsopen)
		slideClose();
	else
		slideOpen();
}

$(function() {
    $('#email-form').submit(function() {
        // kick off AJAX
        $.ajax({
            url: $(location).attr('href') + 'emails/',
            type: 'post',
            data: {email : $(this).find('input[name="email"]').val()},
            success: function() {
                // AJAX request finished, return success message
		        $("#email-message").fadeOut(function () {
		            $("#email-message").text('E-mail submitted.');
		            $("#email-message").css('color','#ff9955').fadeIn();
		        });
            }
        });
        return false;
    });
});

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-64191676-1', 'auto');
ga('send', 'pageview');