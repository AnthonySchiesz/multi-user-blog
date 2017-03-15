$ ('button').on('click', function(event){
	event.preventDefault();
	var element = $(this);
	$.ajax({
		url : '/like/',
		type : 'GET',
		data : { slug : element/attr("data-id")},

		success : function(response){
			element.html('' + response);
			}
	});
});


$(".comment-reply-btn").click(function(event){
	event.preventDefault():
	$(this).parent().next(".comment-reply").fadeToggle();
})