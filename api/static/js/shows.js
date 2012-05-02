(function(){
    $.ajax({
        url: '/v1/shows',
        type: 'POST',
        data: {
            url: 'http://test.com',
            title: 'Test website',
            start_date: '1/1/2012'
        },
        success: function(d){
            console.log(d);
        }
    });

})();
