


$('#button').click(function(event){

	event.preventDefault();
    
    var postlike = $(this).attr("data-like");
    var url = this.href;

    $.get(url, {postlike: postlike}, function(data){
    			
               $('#result').load(' #content', data);
               $('#content').remove();
               
    });
});







// $("#button").click( function(event){

// 	event.preventDefault();

// 	$('#content').remove();

//   	$('#result').load(' #content', function(responseTxt, statusTxt, xhr){
//    	if(statusTxt=='success'){
//    		alert('it went fine learnit');
//    	} else if (statusTxt=='error'){
//   		alert('Not successfuls');
//    	}
//    });

// });
