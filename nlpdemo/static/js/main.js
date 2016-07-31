jQuery(function($) {

	//$(function(){
	//	$('#main-slider.carousel').carousel({
	//		interval: 10000,
	//		pause: false
	//	});
	//});
	$(function(){
		$('#main-slider.carousel').carousel({
			interval: 10000,
			pause: false
		});
		$('#main-slider.carousel').on('slide.bs.carousel', function() {
			var bool_item_01 = $("#div_item_01").hasClass("active");
			var bool_item_02 = $("#div_item_02").hasClass("active");
			// 注意：此处逻辑，容易搞乱
			if(bool_item_01 == true && bool_item_02==false){
				//$("#a_experience").attr("display", "none");
				//$("#a_login").attr("display", "none");
				//$("#div_item_02 .container .carousel-content").append("<ul class=\"portfolio-filter\"><li id=\"li01\"></li><li id=\"li02\"></li></ul>");
				$("#li01").html("<br/><br/><br/>");
				$("#li02").html("<br/><br/><br/>");
			} else if(bool_item_02 == true && bool_item_01 == false){
				$("#li01").html("<a id=\"a_experience\" class=\"btn btn-primary\" href=\"/show/\" style=\"border:0px;\" >体验</a>");
                                $("#li02").html("<a id=\"a_login\" class=\"btn btn-primary\" href=\"/login\"  style=\"border:0px;\" >登录</a>");
			}
		});
	});

	//smooth scroll
	$('.navbar-nav > li').click(function(event) {
		//event.preventDefault();
		var target = $(this).find('>a').prop('hash');
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 500);
	});

	//scrollspy
	$('[data-spy="scroll"]').each(function () {
		var $spy = $(this).scrollspy('refresh')
	})

	//PrettyPhoto
	$("a.preview").prettyPhoto({
		social_tools: false
	});

	//Isotope
	$(window).load(function(){
		$portfolio = $('.portfolio-items');
		$portfolio.isotope({
			itemSelector : 'li',
			layoutMode : 'fitRows'
		});
		$portfolio_selectors = $('.portfolio-filter >li>a');
		//$portfolio_selectors.on('click', function(){
		//	console.log('hi')
		//	$portfolio_selectors.removeClass('active');
		//	$(this).addClass('active');
		//	var selector = $(this).attr('data-filter');
		//	$portfolio.isotope({ filter: selector });
		//	return false;
		//});
	});
});
