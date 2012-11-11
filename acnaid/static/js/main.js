
$(document).ready(function(){	
	if($('#like-us').size() > 0) {
		$('#like-us li').hover(function() {
			$(this).siblings().removeClass('hovered');
			$(this).siblings().children('i').hide();
			$(this).children('i').show();
			$(this).addClass('hovered');
			$(this).siblings().children('.description').hide();
			$(this).children('.description').fadeIn(500);
			}, function() {
		});
	}
	
	if($('#main #promo ul').size() > 0) {
		$("#main #promo ul").carouFredSel({
			pagination : '.pagination',
			scroll : {
				fx : "scroll",
				duration : 800
			}
		});
	}
});

$(window).ready(function(){
	if($('#like-us').size() > 0) {
		$('#like-us li:first-child').addClass('hovered').children('.description').fadeIn(500);
	}	
});
