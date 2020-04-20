/** function for displaying the hover menu on small devicesb **/
$(function(){
	$('#ul-smallscreen1').hide();

	$('#ul-smallscreen2').hide();

	$('#ul-smallscreen3').hide();

	$('#Hollywood-smallscreen').click(function(){
		$('#ul-smallscreen1').hide(1000);
	});
	$('#Hollywood-smallscreen').click(function(){
		$('#ul-smallscreen1').show();
	});
	$('#Nollywood-smallscreen').click(function(){
		$('#ul-smallscreen2').hide(1000);
	});
	$('#Nollywood-smallscreen').click(function(){
		$('#ul-smallscreen2').show();
	});
	$('#Bollywood-smallscreen').click(function(){
		$('#ul-smallscreen3').hide(1000);
	});
	$('#Bollywood-smallscreen').click(function(){
		$('#ul-smallscreen3').show();
	});
	$('a').active(function(){
		$(this).css({'#':'#'});
	});
	setTimeout(function(){
		$('#message').fadeOut('slow');
	}, 2000);
	$('#like-button').click(function(){
		$(this).attr({'class':'disabled'});
	});
});
