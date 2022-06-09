# portfolio-website
Responsive personal website built with flask and bootstrap.

<h1>Some Notes</h1>
<h3>Bouncing Brackets</h3>
<p>The bouncing bracket effect on the page's header is achieved using CSS animation. An animation is applied
to the parent div of each bracket. For example,
<p><em>.bounce-right {animation: bounce-right 4s infinite}</em></p>
<p>Using an @keyframes rule, the transform CSS property is used to change the x position of the div, with the
intervening keyframes consisting of a return to its original x coordinate. Here's a simplified
example:</p>
<p><em>@keyframes bounce-right {0%, 25%, 45% {transform: translateX(0)} 20% {transform: translateX(6px)} 40% 
{transform: translateX(1.5px)}}</em></p>
<p>To adjust the header design responsively, at the width of a mobile screen, the brackets switch from positions on 
the left and right sides of the header div to positions on the top and bottom of the header div. This effect
is accomplished by creating four total brackets, each with a parent div and each placed in the four different positions
described (left, right, top, bottom). Using an @media rule, the top and bottom bracket divs go from zero to full opacity
when the viewport drops below 577 pixels, while the left and right bracket divs do the reverse.</p>
<h3>Slanted background</h3>
<p>The CSS psuedo-element ::before is used with the header div to create the background image, which is filtered
a light blue linear-gradient and rotated using the transform property. Its absolute position causes it to be displayed
behind the header div. In order to keep the bottom of the header div a horizontal line, the header div's overflow
property is set to hidden, meaning the ::before pseudo element's background is hidden anywhere it exceeds the boundaries
of the header div.</p>
<h3>Navbar background</h3>
<p>The same ::before pseudo-element concept is used with the navigation bar background to match the background of the
header div. The intent was to make it feel like a chunk of the header that sticks to the top of the viewport as the user
scrolls down. To do this, it was necessary to split what feels like a single element (the navigation bar) into two: the 
actual navigation bar and its buttons, which remains on top of all the other page elements, and the navigation bar's
background, which is hidden behind the header div until the user scrolls down. The navbar background's z-index is set to
lower than the z-indeces of the header div and the navbar but greater than those of the other page elements.</p>