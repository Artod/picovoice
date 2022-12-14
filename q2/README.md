# Question 2
Q2 [JavaScript, TypeScript] Implement a 5-star widget for an eCommerce site for users to record
a product rating. The widget displays a horizontal row of stars that are either outlined or black
according to the product rating, from left to right. E.g. ★★★☆☆ = rating of 3. Multiple 5-star
widgets can be present on a single page. If a user has not rated a product, the widget will have 5
outlined stars (☆☆☆☆☆). Each product on the page has a UUID. Hovering over the Nth star will
light up stars 1 to N with a grey colour (e.g. ★★★★☆). Clicking a star will record the rating by
sending a request to a web server with enough information to record the product and the rating.
After clicking, the widget will then display the rating the user submitted with black stars (e.g.
★★★★☆). Submitting the rating is handled without refreshing the page.
NOTE: You do not need to implement the backend.

## Answer
The widget can be found in the **`index.html`** file. For the demo, you can simply open the `index.html` in the browser.

This implementation uses HTML to create the 5-star widget for a product with a given UUID, and uses CSS to style the widget. The JavaScript code adds event listeners to handle hover and click events on the stars, and sends the rating to the server using an AJAX request. Note that the actual implementation of the server-side logic to record the product rating is not included in this code.
