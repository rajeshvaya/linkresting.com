App = {
	confirm_before_delete: function(url){
		swal({
				title: "Are you sure?",
				text: "You will not be able to recover this",
				type: "warning",
				showCancelButton: true,
				confirmButtonColor: "#e8273b",
				confirmButtonText: "Yes, delete it!",
				closeOnConfirm: false
			},
			function(){
				//swal("Ok, as you wish", "Going to delete now", "success");
				window.location.href=url;
			}
		);
	}

};
