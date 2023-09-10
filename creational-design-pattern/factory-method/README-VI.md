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

## Khi nào thì sử dụng factory method
1. **Khi bạn muốn tạo đối tượng mà loại đối tượng con cụ thể không được biết trước trong mã nguồn chính (client code)**: Factory Method cho phép bạn tạo đối tượng mà không cần biết concrete class (lớp cụ thể) nào sẽ được tạo. Điều này hữu ích khi bạn muốn giữ cho client code độc lập với các concrete class cụ thể và tạo tính linh hoạt trong việc cấu hình ứng dụng.
2. **Khi bạn muốn mở rộng ứng dụng dễ dàng bằng cách thêm các lớp mới**: Factory Method làm cho việc mở rộng ứng dụng dễ dàng hơn bằng cách thêm các lớp con mới mà không cần sửa đổi mã nguồn hiện có. Bạn chỉ cần tạo một lớp factory mới cho lớp con mới và cấu hình client code để sử dụng factory mới này.
3. **Khi bạn muốn tạo đối tượng dựa trên ngữ cảnh hoặc điều kiện cụ thể**: Factory Method cho phép bạn tạo đối tượng dựa trên điều kiện hiện tại hoặc ngữ cảnh của ứng dụng. Ví dụ, bạn có thể tạo một factory method để tạo đối tượng theo dựa vào ngôn ngữ hiện tại của ứng dụng.
4. **Khi bạn muốn kiểm soát kiểu đối tượng được tạo**: Factory Method cho phép bạn áp dụng logic hoặc kiểm tra trước để quyết định loại đối tượng nào sẽ được tạo. Điều này giúp bạn kiểm soát và tùy chỉnh việc tạo đối tượng theo nhu cầu cụ thể của ứng dụng.
5. **Khi bạn muốn tách biệt quá trình xây dựng đối tượng ra khỏi client code**: Factory Method tách biệt việc xây dựng đối tượng ra khỏi client code, giúp làm cho mã nguồn dễ đọc hơn và tránh sự phức tạp trong việc tạo đối tượng.

>Tóm lại, bạn nên sử dụng Factory Method khi cần tạo đối tượng một cách linh hoạt, duy trì tính linh hoạt trong ứng dụng và giảm sự phụ thuộc vào lớp cụ thể.
## Running
```
python main.py
python example.py
```