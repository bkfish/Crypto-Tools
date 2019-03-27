//
// ---Retro Button---
//
var buttons = document.querySelectorAll('.btn');

for(var i = 0; i < buttons.length; i++) {
  // Click
  buttons[i].addEventListener('mousedown', function() {
    this.classList.add('btn-active');
  });
  buttons[i].addEventListener('mouseup', function() {
    this.classList.remove('btn-active');
  });

  // Hover
  buttons[i].addEventListener('mouseleave', function() {
    this.classList.remove('btn-center', 'btn-right', 'btn-left', 'btn-active');
  });

  buttons[i].addEventListener("mousemove", function(e) {
    var leftOffset = this.getBoundingClientRect().left;
    var btnWidth = this.offsetWidth;
    var myPosX = e.pageX;
    var newClass = "";
    // if on left 1/3 width of btn
    if(myPosX < (leftOffset + .3 * btnWidth) ) {
      newClass = 'btn-left'
    } else {
      // if on right 1/3 width of btn
      if(myPosX > (leftOffset + .65 * btnWidth) ) {
        newClass = 'btn-right';
      } else {
        newClass = 'btn-center';
      }
    }
    // remove prev class
    var clearedClassList = this.className.replace(/btn-center|btn-right|btn-left/gi, "").trim();
    this.className = clearedClassList + " " + newClass;
  });
}


//
// ---Retro Submit Button---
//
var pButton = document.querySelector('.loader-button');

// Click
pButton.addEventListener('mousedown', function() {
  this.classList.add('btn-active');
});
pButton.addEventListener('mouseup', function() {
  this.classList.remove('btn-active');
});


// Classie Helper Functions
// https://github.com/desandro/classie

function classReg( className ) {
  return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
}

// classList support for class management
// altho to be fair, the api sucks because it won't accept multiple classes at once
var hasClass, addClass, removeClass;

if ( 'classList' in document.documentElement ) {
  hasClass = function( elem, c ) {
    return elem.classList.contains( c );
  };
  addClass = function( elem, c ) {
    elem.classList.add( c );
  };
  removeClass = function( elem, c ) {
    elem.classList.remove( c );
  };
}
else {
  hasClass = function( elem, c ) {
    return classReg( c ).test( elem.className );
  };
  addClass = function( elem, c ) {
    if ( !hasClass( elem, c ) ) {
      elem.className = elem.className + ' ' + c;
    }
  };
  removeClass = function( elem, c ) {
    elem.className = elem.className.replace( classReg( c ), ' ' );
  };
}

function toggleClass( elem, c ) {
  var fn = hasClass( elem, c ) ? removeClass : addClass;
  fn( elem, c );
}

var classie = {
  // full names
  hasClass: hasClass,
  addClass: addClass,
  removeClass: removeClass,
  toggleClass: toggleClass,
  // short names
  has: hasClass,
  add: addClass,
  remove: removeClass,
  toggle: toggleClass
};

// transport
if ( typeof define === 'function' && define.amd ) {
  // AMD
  define( classie );
} else {
  // browser global
  window.classie = classie;
}


// Loader Progress Functionality

function extend( a, b ) {
  for( var key in b ) { 
    if( b.hasOwnProperty( key ) ) {
      a[key] = b[key];
    }
  }
  return a;
}

function LoaderButton( el, options ) {
  this.button = el;
  this.options = extend( {}, this.options );
  extend( this.options, options );
  this._init();
}

LoaderButton.prototype.options = {
  statusTime : 1500
};

LoaderButton.prototype._init = function() {
  this._create();
  this._initEvents();
};

LoaderButton.prototype._create = function() {
  var textEl = document.createElement( 'span' );
  textEl.className = 'content';
  textEl.innerHTML = this.button.innerHTML;
  var progressEl = document.createElement( 'span' );
  progressEl.className = 'progress';
  
  var progressInnerEl = document.createElement( 'span' );
  progressInnerEl.className = 'progress-inner';
  progressEl.appendChild( progressInnerEl );
  
  this.button.innerHTML = '';

  this.button.appendChild( textEl );
  this.button.appendChild( progressEl );

  // element for progress bar
  this.progress = progressInnerEl;

  this.progressProp = 'width';
  this._enable();
};

LoaderButton.prototype._setProgress = function( val ) {
  this.progress.style[ this.progressProp ] = 100 * val + '%';
};

LoaderButton.prototype._initEvents = function() {
  var self = this;
  this.button.addEventListener( 'click', function() {
    // disable button
    self.button.setAttribute( 'disabled', '' );
    // add class state-loading to button
    classie.remove( self.progress, 'notransition' );
    classie.add( this, 'state-loading' );

    setTimeout( function() {
      if( typeof self.options.callback === 'function' ) {
        self.options.callback( self );
      }
      else {
        self._setProgress( 1 );
        var onEndTransFn = function( ev ) {
          if( ev.propertyName !== self.progressProp ) { 
            return; 
          }
          this.removeEventListener( 'transitionend', onEndTransFn );
          self._stop();
        };

        self.progress.addEventListener( 'transitionend', onEndTransFn );
      }
    }, 
    200 ); // 200ms timeout
  } );
};

LoaderButton.prototype._stop = function( status ) {
  var self = this;

  setTimeout( function() {
    // fade out progress bar
    self.progress.style.opacity = 0;
    var onEndTransFn = function( ev ) {
      if( ev.propertyName !== 'opacity' ) return;
      this.removeEventListener( 'transitionend', onEndTransFn );
      classie.add( self.progress, 'notransition' );
      self.progress.style[ self.progressProp ] = '0%';
      self.progress.style.opacity = 1;
    };
    
    self.progress.addEventListener( 'transitionend', onEndTransFn );
    
    // add class state-success to button
    if( typeof status === 'number' ) {
      var statusClass = status >= 0 ? 'state-success' : 'state-error';
      classie.add( self.button, statusClass );
      // after options.statusTime remove status icon
      setTimeout( function() {
        classie.remove( self.button, statusClass );
        self._enable();
      }, self.options.statusTime );
    }
    else {
      self._enable();
    }

    // remove class state-loading from the button
    classie.remove( self.button, 'state-loading' );
  }, 100 );
};

// enable button
LoaderButton.prototype._enable = function() {
  this.button.removeAttribute( 'disabled' );
}

// add to global namespace
window.LoaderButton = LoaderButton;


// Initialize Submit Button

[].slice.call( document.querySelectorAll( 'button.loader-button' ) ).forEach( function( bttn ) {
  new LoaderButton( bttn, {
    callback : function( instance ) {
      var progress = 0,
          interval = setInterval( function() {
            progress = Math.min( progress + Math.random() * 0.1, 1 );
            instance._setProgress( progress );

            if( progress === 1 ) {
              instance._stop(1);
              clearInterval( interval );
            }
          }, 200 ); // 200ms interval
    }
  } );
} );