# Order Status Prediction Application

![Home Page Screenshot](https://user-images.githubusercontent.com/92683605/159972315-2bff4282-eb89-477a-bac7-aa6a3686bbf8.PNG)

<h2>About</h2>
Boss Leathers is a small leather products business which has recently started selling its products on Amazon. Currently, it has around 40 SKUs registered in the Indian Marketplace. Over the past few months, it has incurred some loss due to return orders. Now, Boss Leather seeks help to predict the liklihood of a new order being rejected. This would help them in taking necessary actions and subsequently in reducing the loss.

<h2>Objective</h2>
To build an app which would predict the order status upon providing some order details.

<h2>Data Dictionary</h2>
Order details have been scrapped from the Seller Central website using Google App - Web Scraper.

<p>The Order data is stored in an excel file. The columns are:

  *Independent Features:*
  
  | Column  | Description |
  | :-----------: | :-------------: |
  | `order_no`  | Unique Amazon Order Number  |
  | `order_date`  | Date on which the order was placed  |
  | `buyer`  | Name of the buyer  |
  | `ship_city`  | Delivery Address City  |
  | `ship_state`  | Delivery Address State  |
  | `sku`  | Unique identifier of a product  |
  | `description`  | Product description  |
  | `quantity`  | Content Cell  |
  | `item_total`  | Content Cell  |
  | `shipping_fee`  | Charges borne by the seller to ship the item  |

*Label / Target Feature:*
   - `order_status` - Status of the order
  
<h2>Tasks list:</h2>

**The project is in progress and the below tasks will be completed in phases**

  - [x] Order Data Analysis 
  - [x] Model Building (Choosing evaluation metrics, Feature Engineering, Comparing different models)
  - [x] Create an Application
  - [ ] Deploy the Application

<h2>Technologies / Tools:</h2>

  - For Analysis
    - Plotly Express
    - Pandas 
    - Seaborn
    - Python
    - Jupyter Notebook
   
  - For Modelling
    - Sklearn
    - Python
    - Jupyter Notebook

  - App building
    - Python
    - Flask
    - Pycharm
    - HTML
    - CSS
    - Bootstrap

  - Deployment - To be decided

<h2>Future Scope</h2>

Currently, the data extraction is done manually; weekly or fornightly. Going forward perhaps this task can be automated with BeautifulSoup. Also, instead of combining multiple order details csv files, the weekly data can be appended in a common database table which can then be read for model building. To improve the accuracy we can try remodelling with different algorithms. 
From the frontend perspective, validations on the fields will also be added.

