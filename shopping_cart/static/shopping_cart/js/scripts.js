$(document).ready(function(){
    $(".form-select").change(function(event){
        item_id = event.target.id.split("-")[1];
        product_unit_id = $(this).find('option:selected').val();
        $.get("/products/product-unit/" + product_unit_id , function(data, status){
            if(status = "success"){
                $("#unit-price-" + item_id).val(data['price'])
                calculate_item_total(item_id)
            }
          });
       
    })

    $(".quantity").change(function(event){
        item_id = event.target.id.split("-")[1];
        calculate_item_total(item_id)
    })

    $(".confirm-btn").click(function(){
        items = generate_submit_data()
       $.ajax({
            type: "POST",
            url: "/cart/confirm-cart",
            data: JSON.stringify ({"items": items}),
            headers: {
                "X-CSRFToken" : CSRF_TOKEN,
            },
            success: function(result){
                console.log(result)
                if (result['errors'].length > 0){
                    err_str = ""
                    for(var error of result['errors']){
                        err_str += error + "<br>"
                    }
                    x = $("#errors").find("p").html(err_str)
                    $("#errors").show()
                    $(".confirm-btn").prop('disabled', true);
                }else{
                   y =  $("#message").find("p").html(result.message)
                    $("#message").show()
                    $(".confirm-btn").hide()
                }
               
            },
            contentType: "application/json",
            dataType: 'json'
          });
    })
})

function calculate_item_total(item_id){
    $(".confirm-btn").prop('disabled', false);
        $("#errors").hide()
        $("#messages").hide()
    item_price = $("#unit-price-" + item_id).val()
    item_quantity = $("#quantity-" + item_id).val()
    $("#total-price-"+item_id).val(item_price * item_quantity) 
    calculate_cart_total()
}

function calculate_cart_total(){
    var cart_total = 0;
    $(".item-total-price").each(function(){
        cart_total += parseFloat($(this).val())
    })
    $("#cart-total").val(cart_total)
}

function generate_submit_data(){
    var items = []
    $('.card').each(function(){
        item_id = $(this).attr('id')
        var item = {
            id : parseInt(item_id),
            product_unit_id : parseInt($("#unit-" + item_id).val()),
            price: parseFloat($("#unit-price-" + item_id).val()),
            quantity: parseFloat($("#quantity-" + item_id).val()),
        }
        items.push(item);
    })
    return items
}

