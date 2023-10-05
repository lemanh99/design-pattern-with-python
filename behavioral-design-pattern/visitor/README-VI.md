## Source

https://refactoring.guru/design-patterns/visitor

## Cốt lõi:

> Mẫu thiết kế Visitor là một mẫu thiết kế hành vi cho phép bạn tách biệt các thuật toán khỏi các đối tượng mà chúng
> hoạt động lên

## Structure

![alt tag](visitor.png)

Các bước tạo visitor chính:

1. Xác định cấu trúc đối tượng: Xác định cấu trúc đối tượng mà bạn muốn thực hiện các thao tác hoặc xử lý trên đó. Đảm
   bảo rằng cấu trúc này bao gồm các lớp đối tượng khác nhau mà bạn muốn xử lý bằng cách sử dụng Mẫu Visitor.
2. Tạo Interface cho Visitor: Định nghĩa một giao diện hoặc lớp trừu tượng cho Visitor. Giao diện này sẽ định nghĩa các
   phương thức "visit" cho mỗi loại đối tượng mà bạn muốn xử lý. Các phương thức này thường sẽ có các tham số đối tượng
   cụ thể.
3. Triển khai lớp Visitor cụ thể: Tạo các lớp con triển khai giao diện Visitor. Mỗi lớp con này sẽ triển khai các phương
   thức "visit" cho các loại đối tượng khác nhau.
4. Thêm phương thức "accept" vào các lớp đối tượng: Trong mỗi lớp đối tượng mà bạn muốn xử lý bằng Mẫu Visitor, thêm một
   phương thức "accept" (hoặc tùy chọn khác) để chấp nhận một đối tượng Visitor và chuyển điều khiển cho Visitor để thực
   hiện các thao tác hoặc xử lý.
5. Thực hiện các thao tác hoặc xử lý trong phương thức "visit" của Visitor: Trong các phương thức "visit" của lớp
   Visitor, thực hiện các thao tác hoặc xử lý cụ thể cho từng loại đối tượng. Điều này có nghĩa là bạn sẽ triển khai
   logic xử lý cụ thể cho mỗi loại đối tượng trong phương thức "visit" tương ứng.
6. Sử dụng Mẫu Visitor: Tạo một đối tượng Visitor cụ thể và gọi phương thức "accept" trên các đối tượng trong cấu trúc
   đối tượng để bắt đầu quá trình xử lý hoặc thao tác.

## Description

### Mục đích

Mục đích chính của Mẫu thiết kế Visitor (Visitor Design Pattern) là cho phép bạn thực hiện các thao tác hoặc xử lý trên
một cấu trúc đối tượng phức tạp mà không cần thay đổi cấu trúc của các lớp đối tượng trong cấu trúc đó. Dưới đây là các
mục đích cụ thể của Mẫu Visitor:

1. **Tách biệt các thao tác từ cấu trúc đối tượng:** Visitor tách biệt các thao tác hoặc xử lý ra khỏi cấu trúc đối
   tượng chứa chúng. Điều này giúp duy trì tính độc lập giữa thao tác và đối tượng, làm cho mã nguồn dễ bảo trì hơn.
2. **Cho phép mở rộng chức năng mà không cần sửa đổi mã nguồn của đối tượng:** Bạn có thể thêm các visitor mới để thực
   hiện các thao tác mới trên cấu trúc đối tượng mà không cần sửa đổi lớp đối tượng hiện có. Điều này giúp tạo điều kiện
   cho tính linh hoạt và bảo trì mã nguồn.
3. **Hỗ trợ xử lý đa hình (polymorphism):** Visitor cho phép bạn thực hiện xử lý đa hình trên đối tượng cơ sở và các lớp
   con của nó. Điều này giúp bạn thực hiện các thao tác đúng với kiểu thực tế của đối tượng.
4. **Phân tách loại đối tượng và các thao tác hoặc xử lý:** Visitor giúp phân tách loại đối tượng và các thao tác hoặc
   xử lý cho loại đối tượng đó. Bạn có thể triển khai các visitor riêng biệt cho từng loại đối tượng, tạo điều kiện cho
   cách tổ chức mã nguồn hiệu quả.
5. **Hỗ trợ tiếp cận đối tượng theo chiều sâu (deep traversal):** Visitor cho phép bạn thực hiện tiếp cận đối tượng theo
   chiều sâu trong cấu trúc đối tượng phức tạp, nếu cần thiết. Bạn có thể điều hướng và xử lý các thành phần con của đối
   tượng một cách dễ dàng.
6. **Thực hiện các mô hình phân tích tĩnh (static analysis):** Visitor thường được sử dụng trong các công cụ phân tích
   tĩnh để thực hiện kiểm tra lỗi, tạo báo cáo, hoặc thu thập thông tin về mã nguồn.

## Khi nào thì sử dụng visitor

1. **Khi bạn muốn thực hiện các thao tác hoặc xử lý trên một cấu trúc đối tượng phức tạp:** Mẫu Visitor cho phép bạn
   định nghĩa các thao tác hoặc xử lý khác nhau cho các đối tượng trong một cấu trúc đối tượng phức tạp mà không cần
   thay đổi lớp của chúng.
2. **Khi lớp đối tượng có sẵn và không thể thay đổi (immutable):** Nếu bạn không thể sửa đổi lớp đối tượng (ví dụ: lớp
   từ thư viện bên ngoài hoặc lớp đã được ổn định), Mẫu Visitor cho phép bạn thêm các thao tác hoặc xử lý mới cho đối
   tượng mà không cần sửa đổi mã nguồn của đối tượng đó.
3. **Khi bạn muốn tách biệt các thao tác từ cấu trúc đối tượng: ** Mẫu Visitor tách biệt các thao tác hoặc xử lý ra khỏi
   cấu trúc đối tượng chứa chúng, giúp bạn duy trì tính độc lập và linh hoạt trong mã của bạn.
4. **Khi có nhiều loại đối tượng và bạn muốn thêm các thao tác hoặc xử lý mới mà không cần sửa đổi các lớp đối tượng:**
   Mẫu Visitor cho phép bạn thêm các "visitor" mới mà không cần sửa đổi các lớp đối tượng hiện có. Điều này hữu ích khi
   bạn có nhiều loại đối tượng và muốn thêm chức năng mà không ảnh hưởng đến các đối tượng hiện có.
5. **Khi bạn muốn thực hiện xử lý đa hình (polymorphic) trên đối tượng cơ sở và các lớp con của nó:** Mẫu Visitor cho
   phép bạn thực hiện xử lý đa hình trên đối tượng cơ sở và gọi đúng phương thức của đối tượng dựa trên kiểu thực tế của
   nó.
6. **Khi bạn muốn áp dụng một chức năng cụ thể cho một nhóm lớp đối tượng liên quan mà không cần thay đổi chúng:** Mẫu
   Visitor cho phép bạn xác định các chức năng cụ thể cho một nhóm lớp đối tượng liên quan bằng cách triển khai các
   visitor riêng biệt cho nhóm đó.

Ví dụ phổ biến của việc sử dụng Mẫu Visitor bao gồm thực hiện việc thống kê các đối tượng trong một cấu trúc cây, thực
hiện các biểu đồ phân tích tĩnh (static analysis) trên mã nguồn, và xử lý các tác vụ trên cấu trúc dữ liệu phức tạp như
cây AST (Abstract Syntax Tree) trong ngôn ngữ lập trình.

## Running

```
python main.py
python example.py
```