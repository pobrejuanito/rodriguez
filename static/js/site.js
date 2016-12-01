(function($) {

        var amountScrolled = 300;
        $(window).scroll(function() {
        	if ( $(window).scrollTop() > amountScrolled ) {
        		$('#toTop').fadeIn('slow');
        	} else {
        		$('#toTop').fadeOut('slow');
        	}
        });

        $('#toTop').click(function(e) {
        	$('html,body').animate({
        		scrollTop: 0
        	}, 'slow');
        	return false;
        });

        $('ul.menu').find('a').click(function(e){
            var $href = $(this).attr('href');
            var $anchor = $('#'+$href).offset();
            $('html, body').animate({
                scrollTop: $anchor.top
            }, 'slow');
            return false;
        });
})(jQuery);
