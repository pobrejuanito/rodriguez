(function($) {
        // You pass-in jQuery and then alias it with the $-sign
        // So your internal code doesn't change
        var amountScrolled = 300;
        $(window).scroll(function() {
        	if ( $(window).scrollTop() > amountScrolled ) {
        		$('#toTop').fadeIn('slow');
        	} else {
        		$('#toTop').fadeOut('slow');
        	}
        });

        $('#toTop').click(function() {
        	$('html,body').animate({
        		scrollTop: 0
        	}, 'slow');
        	return false;
        });
})(jQuery);
