/** function for displaying the hover menu on small devicesb **/
$(function(){
	$('#ul-smallscreen1').hide();

	$('#ul-smallscreen2').hide();

	$('#ul-smallscreen3').hide();

	//the video slide
	$('#frame2').hide();
	$('#frame3').hide();
	$('#frame4').hide();



	$('#view-clip-2').click(function(){
		$('#frame1').hide();
		$('#frame2').show();
		$('#frame3').hide();
		$('#frame4').hide();
		$(this).attr({'class':'btn-success btn-lg'});



	})
	$('#view-clip-1').click(function(){
		$('#frame1').show();
		$('#frame2').hide();
		$('#frame3').hide();
		$('#frame4').hide();
		$(this).attr({'class':'btn-success btn-lg'});
		

	})
	$('#view-clip-3').click(function(){
		$('#frame1').hide();
		$('#frame2').hide();
		$('#frame3').show();
		$('#frame4').hide();
		$(this).attr({'class':'btn-success btn-lg'});
		

	})

	$('#view-clip-4').click(function(){
		$('#frame1').hide();
		$('#frame2').hide();
		$('#frame3').hide();
		$('#frame4').show();
		$(this).attr({'class':'btn-success btn-lg'});
		

	});

	//the video slide end

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
	$('#burger-menu').click(function(){
		$('#libby').slideToggle();
	});
	$('#cancel-button').click(function(){
		$('#message').css({'display':'none'});
	});
	setTimeout(function(){
		$('#message').fadeOut('slow');
	}, 2000);
	$('#like-button').click(function(){
		$(this).attr({'class':'disabled'});
	});
});
