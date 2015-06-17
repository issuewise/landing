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