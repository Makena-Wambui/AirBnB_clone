Inline styling : when we use the style attribute within a HTML Element.
For example:
<header style="color: #f00;">

To refer to a CSS file within a HTML Document, use link element in head element plus 'rel' and 'href' attibutes.
I used a relative url for the images that is the logo and icon in the images folder.

The section element is used to divide the content into logical sections or subsections.

The button HTML element is an interactive element that can be clicked by a user to perform an action, such as submitting a form or opening a dialog
Example: <button type="button">Click Me!</button>

There are two main types of HTML lists:
1. unordered lists (ul) and 
2. ordered lists (ol).
Unordered lists display the items with bullets, while ordered lists display the items with numbers or letters.

The li tag defines a list item.
The li tag is used inside ordered lists(ol), unordered lists (ul), and in menu lists (menu).

The CSS flex property is a shorthand property for:flex-grow, flex-shrink or flex-basis.
The flex property sets the flexible length on flexible items.
If the element is not a flexible item, the flex property has no effect.

Integrity attribute
-----------------------
used primarily for ensuring the integrity of external resources (such as stylesheets, scripts, or fonts) loaded by a web page.
It defines a hash value (similar to a checksum) that corresponds to the expected content of the resource.
If the content has been tampered with (e.g., due to a compromised server or CDN), the browser will refuse to execute the resource.
Essentially, the integrity attribute prevents loading of different (potentially malicious) resources.
The integrity and crossorigin attributes are used in the script and link tags.

Cross origin Attribute
------------------------
The crossorigin attribute helps manage security and access control for cross-origin resources.
You must include the crossorigin attribute to check the integrity of the resource when the resource is not hosted on the same origin server where your web application is hosted. Without crossorigin attribute, the browser will load the resource as if the integrity attribute was not set, effectively losing all the security SRI brings in.
crossorigin="anonymous" means that no credential is sent to the cross-origin site where your application’s third party resource is hosted.

FONT AWESOME
---------------
Font Awesome provides a vast collection of scalable vector icons that you can easily incorporate into your web projects.
Include Font Awesome CSS in the link tag's href attribute value.
Font Awesome icons are designed to be used with inline elements like i or span
To include an icon, use the fa prefix followed by the icon’s name. For example:
	<i class="fa fa-car"></i>
You can adjust the icon size and color using CSS styles.
	<i class="fa fa-car" style="font-size:48px;"></i>
	<i class="fa fa-car" style="font-size:60px; color:red;"></i>

To increase the icon size relative to its container, use classes like fa-lg, fa-2x, fa-3x, fa-4x, or fa-5x. For example:
	<i class="fa fa-car fa-lg"></i>
	<i class="fa fa-car fa-2x"></i>

Replace default bullets in unordered lists with Font Awesome icons:
	<ul class="fa-ul">
  		<li><i class="fa-li fa fa-check-square"></i> List icons</li>
  		<li><i class="fa-li fa fa-spinner fa-spin"></i> List icons</li>
  		<li><i class="fa-li fa fa-square"></i> List icons</li>
	</ul>

Bordered and Pulled Icons:
Use classes like fa-border, fa-pull-right, or fa-pull-left for pull quotes or article icons:
	<i class="fa fa-quote-left fa-3x fa-pull-left fa-border"></i>
	Lorem ipsum dolor sit amet...

Add animation to icons using the fa-spin class:
	<i class="fa fa-spinner fa-spin"></i>
	<i class="fa fa-circle-o-notch fa-spin"></i>
	<i class="fa fa-refresh fa-spin"></i>

