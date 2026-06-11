def display_products(products): 
    print("\n=== DANH SÁCH KHO HÀNG ===")
    if not products: 
        print("Danh sách hiện tại đang trống!")
        return 
    
    header = f"| {'Mã SP':<10} | {'Tên sản phảm':<35} | {'Đơn giá':<15} | {'Số lượng':<10} | {'Tổng giá trị':<15} | {'Trạng thái':<20} |"
    print("-"*len(header))
    print(header)
    print("-"*len(header)) 
    
    for pr in products:
        row = f"| {pr['id']:<10} | {pr['name_product']:<35} | {pr['amount']:<15,.0f} | {pr['stock']:<10} | {pr['safety_stock']:<15,.0f} | {pr['status']:<20} |"
        print(row)
    print("-"*len(header)) 
    

    
def calculate_total_value(amount,stock): 
    return amount * stock

def classif_stock(stock,safety_stock): 
    if stock == 0:
        return 'Hết hàng'
    elif stock < safety_stock:
        return 'Cảnh báo(Cần nhập hàng)'
    elif safety_stock <= stock <= safety_stock*3: 
        return 'An toàn'
    else: 
        return 'Quá tải(Thặng dư)' 
    
def find_products(products,pr_id): 
    for i,pr in enumerate(products): 
        if pr['id'] == pr_id.upper():
            return i
        
    return -1 

def get_valid_id(products): 
    while True: 
        pr_id = input("Nhập mã sản phẩm").strip().upper()
        if not pr_id: 
            print("Mã sản phẩm không được để trống!")
            continue 
        if find_products(products,pr_id) != -1: 
            print("Mã sản phẩm đẫ tồn tại trong hệ thống!")
            continue 
        return pr_id 
    
def get_valid_name_product(): 
    while True: 
        name_product = input("Nhập tên sản phẩm: ").strip().capitalize()
        if not name_product: 
            print("Tên sản phẩm không được để trống!")
            continue 
        return name_product

def get_valid_amount(): 
    while True: 
        try: 
            amount = float(input("Nhập đơn giá vốn (>0): ").strip())
            if amount <= 0: 
                print("Đơn giá không được âm!")
                continue 
            if not amount: 
                print("Không được để trống!")
                continue 
            return amount 
        except ValueError: 
            print("Vui lòng nhập lại đơn giá!")
            
def get_valid_stock(): 
    while True: 
        try: 
            stock = float(input("Nhập số lượng tồn kho (>0): ").strip())
            if stock <= 0: 
                print("Số lượng tồn kho không được âm!")
                continue 
            if not stock: 
                print("Không được để trống!")
                continue 
            return stock 
        except ValueError: 
            print("Vui lòng nhập lại số lượng !")
            
def get_valid_safety_stock(): 
    while True: 
        try: 
            safety_stock = float(input("Nhập định mức tối thiểu (>0): ").strip())
            if safety_stock <= 0: 
                print("Định mức tối thiểu không được âm!")
                continue 
            if not safety_stock: 
                print("Không được để trống!")
                continue 
            return safety_stock 
        except ValueError: 
            print("Vui lòng nhập lại định mức !")

def add_products(products): 
    print("\n=== THÊM SẢN PHẨM ===")
    pr_id = get_valid_id(products)
    name_product =get_valid_name_product()
    amount = get_valid_amount()
    stock = get_valid_stock()
    safety_stock = get_valid_safety_stock() 
    
    total_value = calculate_total_value(amount,stock)
    status = classif_stock(amount,safety_stock) 
    
    new_products = {
        'id': pr_id,
        'name_product':name_product,
        'amount': amount,
        'stock':stock,
        'safety_stock': safety_stock, 
        'total_value': total_value,
        'status': status
    }
    products.append(new_products)
    print(">> Đã thêm thành công đơn hàng")
    

def delete_products(products): 
    print("\n=== XÓA SẢN PHẨM ===")
    if not products:
        print("Hiện tại không có sản phẩm trong hệ thống nên không thể xóa!")
        return 
    
    pr_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()
    if not pr_id: 
        print("Mã sản phẩm không được để trống!")
        return 
    
    index = find_products(products,pr_id)
    if index == -1: 
        print("Lỗi: Không tìm thấy mã trong danh sách!") 
        return 
    
    confirm = input("Bạn có chắc muốn xóa sản phẩm này khỏi danh mục không (Y/N): ").strip().upper()
    
    if confirm == "Y": 
        products.pop(index)
        print("Đã xóa thành công mã sản phẩm này!")
    else:
        print(">> Hủy thao tác")


def search_products(products): 
    print("\n=== TÌM KIẾM SẢN PHẨM ===")
    if not products:
        print("Hiện tại không có sản phẩm trong hệ thống nên không thể tìm kiếm!")
        return 
    
    keyword = input("Nhập mã sản phẩm hoặc tìm gần đúng dựa vào tên sản phẩm: ").strip().upper()
    results = []
    if not keyword: 
        print("Mã sản phẩm không được để trống!")
        return 
    
    for pr in products:
        if keyword == pr['id'] or keyword in pr['name_product'].upper():
            results.append(pr) 
            
    if not results: 
        print("Không tìm từ khóa trong danh sách!")
    else:
        print(f"Tìm thấy {len(results)} kết quả")
        display_products(results) 


def statistical_status(products): 
    print("\n=== THỐNG KÊ TRẠNG THÁI ===")
    if not products:
        print("Hiện tại không có sản phẩm trong hệ thống nên không thể thống kê!")
        return 

    stats = {'Hết hàng': 0,'Cảnh báo(Cần nhập hàng)': 0,'An toàn': 0 ,'Quá tải(Thặng dư)': 0}
    
    for pr in products: 
        stats[pr['status']] += 1 
        
    for product,count in stats.items(): 
        print(f"Trạng thái ({product:<15}): {count} sản phẩm")
    
    
def main():   
    products = [
        {
            'id': 'SP001',
            'name_product':'Chuot khong day Logitech',
            'amount': 250000,
            'stock':15,
            'safety_stock': 20 , 
            'total_value': 3750000,
            'status': 'Cảnh báo' 
        }
    ]
    
    while True:
        print("\n"+ "="*75)
        print("     HỆ THỐNG QUẢN LÝ DANH MỤC SẢN PHẨM VÀ HÀNG TỒN KHO     ")
        print("="*75)
        print("""
1. Hiển thị danh sách kho hàng
2. Khai báo sản phẩm mới
3. Cập nhật số lượng và giá vốn
4. Xóa sản phẩm khỏi danh mục 
5. Tìm kiếm sản phẩm 
6. Thống kê trạng thái kho hàng 
7. Thoát chương trình
            """) 
        print("="*75) 
        choice = input("Nhập chức năng (1-7): ").strip()
        if not choice: 
            print("Lỗi: Vui lòng không được để trống!")
            continue
        
        match choice: 
            case "1":
                display_products(products)
            case "2": 
                add_products(products) 
            case "4":
                delete_products(products) 
            case "5":
                search_products(products) 
            case "6": 
                statistical_status(products) 
            case "7":
                print("Cảm ơn bạn sử dụng hệ thống quản lý!")
                break 
            case _: 
                print("Lỗi: Vui lòng nhập lại chức năng từ (1-7) trong hệ thống") 
                
                
if __name__ == "__main__":
    main() 