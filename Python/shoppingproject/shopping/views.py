from django.shortcuts import render
from django.http import HttpResponseRedirect    #追加
from django.urls import reverse    #追加
from django.template.response import TemplateResponse
from shopping.models import Product   #モデルをインポート

#インポートしたモデルからデータを取得して返す、product_listというview関数
def product_list(request):
	products = Product.objects.order_by('name')
	return TemplateResponse(request, 'shopping/product_list.html',{'products': products})
#第1引数：view関数の引数にあるrequest、第2引数：テンプレートへのパス、第３引数：辞書{}を指定
 

# 404ページ   追加
from django.http import Http404

# 商品詳細ページ   追加
def product_detail(request, product_id):
		try:
			product = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
				raise Http404
        #問③-2 product_list view関数を参考に、ここに記述しましょう。
		return TemplateResponse(request, 'shopping/product_detail.html',{'product': product})

# 一つ前で作ったproduct_cart関数の書き換え
def product_cart(request):
		cart = request.session.get('cart')
		if cart:
				products = []
				for product_id in cart:
						try:
								product = Product.objects.get(id=product_id)
								products.append(product)
						except Product.DoesNotExist:
								pass
		else:
				products = []

		total_price = 0
		for product in products:
				total_price += product.price

		return TemplateResponse(request, 'shopping/product_cart.html',{'products': products,'total_price': total_price})

# カート追加機能
def cart_add(request, product_id):
		if not Product.objects.filter(id=product_id).exists():
				raise Http404

		cart = request.session.get('cart')
		if cart:
				cart.append(product_id)
				request.session['cart'] = cart
		else:
				request.session['cart'] = [product_id]
		return HttpResponseRedirect(reverse('product_list'))

# カートから削除機能
def cart_delete(request, product_id):
		cart = request.session.get('cart')
		if cart:
				filtered = []
				for p in cart:
					if p != product_id:
							filtered.append(p)
				request.session['cart'] = filtered
		return HttpResponseRedirect(reverse('product_cart'))



