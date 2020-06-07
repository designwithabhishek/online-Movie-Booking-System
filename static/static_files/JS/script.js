//all objects

let obj1 = document.getElementById('movie-info');
let obj2 = document.getElementById('cast');
let obj3 = document.getElementById('reviews');
content = document.getElementsByClassName('visibility-change');

//flags
var section1_counter = 1;
var section2_counter = 0;
var section3_counter = 0;

//variable
active_object = obj1; //initial

/*
function initiatefourth() {
  obj3.removeEventListener('transitionend', initiatefourth);
  obj3.onwheel = function(e) {
    obj3.style.width = '0px';
    obj3.addEventListener('transitionend', hidereview);
    e.stopPropagation();
  };
}
function initiatethird() {
  obj2.removeEventListener('transitionend', opacitychange);
  obj2.removeEventListener('transitionend', initiatethird);
  obj2.onwheel = function(e) {
    //alert('obj2');
    if (e.deltaY < 0) {
      obj3.style.visibility = 'visible';
      obj3.style.width = '100%';
      obj3.addEventListener('transitionend', initiatefourth);
      e.stopPropagation();
    } else {
      for (i = 0; i < content.length; i++) {
        content[i].style.opacity = '0';
      }
      content[i - 1].addEventListener('transitionend', backtomovieinfo);
      e.stopPropagation();
    }
  };
}
*/
function next_section() {
  obj2.removeEventListener('transitionend', next_section);
  section2_counter = 1;
}

function previous_section() {
  alert('calling previous section');
  active_object.style.visibility = 'hidden';
  if (active_object == obj2) section1_counter = 1;
  else if (active_object == obj3) section2_counter = 1;
  active_object.removeEventListener('transitionend', previous_section);
  //calculateheight();
  //active_object.addEventListener('transitionend', calculateheight);
}

function fade(e) {
  obj2.removeEventListener('transitionend', fade);
  for (i = 0; i < content.length; i++) {
    content[i].style.visibility = 'visible';
    content[i].style.opacity = '1';
  }
  obj2.addEventListener('transitionend', next_section);
}

function unfade(e) {
  alert('HEllo');
  if (active_object == obj2)
    content[content.length - 1].removeEventListener('transitionend', unfade);
  else if (active_object == obj3)
    active_object.removeEventListener('transitionend', unfade);
  active_object.style.width = '0px';
  active_object.addEventListener('transitionend', previous_section);
}
/*
function calculateheight() {
  alert('calling calculateheight');
  active_object.removeEventListener('transitionend', calculateheight);
  if (forward == 1) {
    alert('Calling forward');
    b = getComputedStyle(active_object).getPropertyValue('height');
    alert(b);
  } else {
    alert('calling backward');
    b = getComputedStyle(previous_object).getPropertyValue('height');
    alert(b);
  }
  a = document.getElementById('movie-data');
  a.style.height = b;
}
*/
/*
function backtomovieinfo() {
  for (i = 0; i < content.length; i++) {
    content[i].style.visibility = 'hidden';
  }
  obj2.style.width = '0px';
  content[i - 1].removeEventListener('transitionend', backtomovieinfo);
  obj2.addEventListener('transitionend', hidecast);
  /*ob2.addEventListener('transitionend', function() {
      ob2.style.visibility = 'hidden';
    });
}
function hidecast() {
  obj2.style.visibility = 'hidden';
  obj2.removeEventListener('transitionend', hidecast);
}

function hidereview() {
  obj3.style.visibility = 'hidden';
  obj3.removeEventListener('transitionend', hidereview);
}
*/
//first screen

obj1.onwheel = function(e) {
  if (section1_counter == 1) {
    obj2.style.visibility = 'visible';
    obj2.style.width = '100%';
    section1_counter = 0;
    active_object = obj2;
    active_object.addEventListener('transitionend', fade);
    e.stopPropagation();
  }
};

obj2.onwheel = function(e) {
  if (section2_counter == 1) {
    section2_counter = 0;
    if (e.deltaY < 0) {
      obj3.style.visibility = 'visible';
      obj3.style.width = '100%';
      active_object = obj3;
      section3_counter = 1;
      forward = 1;
      //obj3.addEventListener('transitionend', calculateheight);
      e.stopPropagation();
    } else {
      for (i = 0; i < content.length; i++) {
        content[i].style.opacity = 0;
      }
      active_object = obj2;
      content[content.length - 1].addEventListener('transitionend', unfade);
    }
  }
};
obj3.onwheel = function(e) {
  alert('section3');
  alert(section3_counter);
  if (section3_counter == 1) {
    active_object = obj3;
    previous_object = obj2;
    forward = 0;
    unfade();
    //active_object.addEventListener('transitionend', unfade);
  }
};
// second screen

// third screen
