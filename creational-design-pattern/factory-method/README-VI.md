## Source
https://refactoring.guru/design-patterns/factory-method
## Cốt lõi:
>"Factory Method" cung cấp một interface cho việc tạo đối tượng trong một lớp cha, nhưng cho phép các lớp con thay đổi loại đối tượng sẽ được tạo ra.
## Structure
![alt tag](factory_method.png)

Các bước tạo factory method:
1. Xác định interface cho Factory Method
2. Xây dựng Factory Classes (Các lớp Factory)
3. Xác định các lớp cụ thể (Concrete Classes)
4. Xây dựng Factory Method
5. Sử dụng Factory Method

## Description

### Mục đích
Factory Method là một design pattern trong lập trình hướng đối tượng (OOP) có mục đích chính là tạo ra một giao diện (interface) để tạo đối tượng (object), nhưng để concretely implement việc tạo đối tượng này, ta để cho các lớp con (subclasses) quyết định. Factory Method giúp loại bỏ việc gắn kết giữa mã nguồn và lớp cụ thể mà chúng ta muốn tạo, tạo sự linh hoạt và mở rộng trong quá trình tạo đối tượng.
Dưới đây là một số mục đích chính của Factory Method trong design pattern:

1. Độc lập với lớp cụ thể (Concrete Class Independence): Factory Method cho phép bạn tạo đối tượng mà không cần biết lớp cụ thể nào đang được tạo. Thay vì tạo đối tượng bằng cách gọi trực tiếp constructor của lớp cụ thể, bạn gọi một phương thức factory để tạo đối tượng.

2. Mở rộng và thay đổi dễ dàng (Easy Extensibility and Modification): Bằng cách sử dụng Factory Method, bạn có thể dễ dàng mở rộng ứng dụng để thêm các lớp cụ thể mới mà không cần thay đổi mã hiện có. Điều này giúp bạn duy trì tính linh hoạt và tránh việc phá vỡ các phần khác của mã nguồn.

3. Tạo đối tượng dựa trên ngữ cảnh (Context-Based Object Creation): Factory Method cho phép bạn chọn lớp cụ thể để tạo đối tượng dựa trên ngữ cảnh hoặc điều kiện hiện tại của ứng dụng. Ví dụ, bạn có thể tạo một factory method để tạo đối tượng theo dựa vào ngôn ngữ hiện tại của ứng dụng.

4. Tách biệt quá trình xây dựng đối tượng (Separation of Object Construction): Factory Method tách biệt việc xây dựng đối tượng ra khỏi client code, giúp làm cho mã nguồn dễ đọc hơn và giảm sự phức tạp trong việc tạo đối tượng.

5. Kiểm soát kiểu đối tượng (Control over Object Types): Factory Method cho phép bạn kiểm soát kiểu đối tượng được tạo bằng cách áp dụng logic trong factory method. Bạn có thể áp dụng các điều kiện hoặc kiểm tra trước khi quyết định tạo đối tượng nào.

Tóm lại, Factory Method là một design pattern quan trọng trong OOP giúp bạn quản lý quá trình tạo đối tượng một cách linh hoạt và dễ dàng mở rộng mã nguồn của bạn.

## Running
```
python main.py
python example.py
```