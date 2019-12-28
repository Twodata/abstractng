

$('a.likereview').click(function(event){

	event.preventDefault();
    
    var reviews = $(this).attr("data-like");
    var url = this.href;

    $.get(url, {reviews: reviews}, function(data){

    		 $('#content').load(' #content', data);
         	 // $('#content').remove();   		
			alert('Abstract at last');
               
    });
});




$('a.delreview').click(function(event){

	event.preventDefault();
    
    var reviews = $(this).attr("data-like");
    var url = this.href;

    $.get(url, {reviews: reviews}, function(data){

    		 $('#content').load(' #content', data);
         	 // $('#content').remove();   		
			alert('reviewdel at last');
               
    });
});



$('a.msgdel').click(function(event){

    event.preventDefault();
    
    var reviews = $(this).attr("data-like");
    var url = this.href;

    $.get(url, {reviews: reviews}, function(data){

             $('#msgcontent').load(' #msgcontent', data);
             // $('#content').remove();         
            alert('msgdel at last');
               
    });
});

