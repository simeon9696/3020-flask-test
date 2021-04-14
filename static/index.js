if ( window.history.replaceState ) {
    //this is to prevent form resubmission on page refresh, if the last request was POST
    window.history.replaceState( null, null, window.location.href );
  }