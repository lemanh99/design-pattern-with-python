## Source

https://refactoring.guru/design-patterns/decorator

## Cốt lõi:

> Decorator là một mẫu thiết kế cấu trúc cho phép bạn đính kèm các hành vi mới vào các đối tượng bằng cách đặt những đối
> tượng này vào bên trong các đối tượng bọc đặc biệt chứa các hành vi.

## Structure

![alt tag](decorator.png)

Các bước tạo một decorator

1. **Xác định interface hoặc lớp cơ sở (base class):** Đầu tiên, bạn cần xác định interface hoặc lớp cơ sở (base class)
   mà tất cả các decorator và đối tượng cần mở rộng sẽ thực hiện. Đây là lớp cơ sở cho các đối tượng và decorator của
   bạn.
2. **Tạo lớp cơ sở cho đối tượng cần mở rộng:** Định nghĩa lớp cơ sở hoặc interface cho đối tượng cần mở rộng. Đây là
   đối tượng mà bạn muốn mở rộng chức năng của nó bằng cách sử dụng decorator.
3. **Tạo các decorator:** Định nghĩa các lớp decorator con mà bạn muốn sử dụng để mở rộng chức năng của đối tượng cơ sở.
   Mỗi decorator sẽ kế thừa từ lớp cơ sở hoặc triển khai giao diện chung.
4. **Thêm thuộc tính để lưu trữ đối tượng gốc:** Trong mỗi decorator, thêm một thuộc tính để lưu trữ đối tượng gốc hoặc
   decorator trước đó. Điều này cho phép bạn chuỗi các decorator lại với nhau.
5. **Triển khai phương thức của decorator:** Triển khai các phương thức của decorator để mở rộng hoặc thay đổi hành vi
   của đối tượng gốc. Thông thường, bạn sẽ gọi phương thức của đối tượng gốc và sau đó thêm hoặc thay đổi hành vi theo
   cách mong muốn.
6. **Tạo đối tượng decorator:** Khi bạn muốn mở rộng chức năng của một đối tượng cụ thể, tạo một đối tượng decorator và
   truyền đối tượng gốc vào nó. Sau đó, bạn có thể sử dụng đối tượng decorator này như một đối tượng thông thường.

## Description

### Mục đích

1. **Mở rộng chức năng một cách linh hoạt:** Decorator cho phép bạn thêm hoặc loại bỏ các tính năng từ một đối tượng mà
   không ảnh hưởng đến các đối tượng khác trong hệ thống. Bạn có thể kết hợp nhiều decorator lại với nhau để tạo ra các
   kết hợp chức năng khác nhau.
2. **Tránh sử dụng quá nhiều class con:** Thay vì tạo một lớp con riêng biệt cho mỗi biến thể của đối tượng, bạn có thể
   sử dụng decorator để thêm chức năng mà không cần tạo quá nhiều lớp con. Điều này giúp tránh sự phức tạp và tăng sự
   linh hoạt trong quản lý code.
3. **Tách biệt việc thay đổi và mở rộng chức năng:** Decorator giúp tách biệt việc thay đổi chức năng của một đối tượng
   và đối tượng gốc, giúp code dễ đọc và bảo trì hơn. Bạn có thể tạo các decorator riêng biệt để mở rộng chức năng mà
   không cần sửa đổi code của đối tượng gốc.
4. **Thực hiện nguyên tắc "đóng cho sửa":** Decorator giúp tuân thủ nguyên tắc "đóng cho sửa" (Open/Closed Principle)
   trong thiết kế phần mềm. Điều này có nghĩa là bạn có thể mở rộng chức năng của một đối tượng mà không cần phải sửa
   đổi code hiện có.
5. **Phân cấp chức năng:** Bạn có thể tạo một loạt các decorator có cấp độ khác nhau để áp dụng chức năng theo cách có
   thứ tự. Điều này giúp quản lý và kiểm soát chức năng mở rộng.

## Khi nào thì sử dụng decorator

Decorator design pattern được sử dụng khi bạn muốn thêm hoặc mở rộng chức năng của một đối tượng mà không cần phải sửa
đổi lớp cơ sở của đối tượng đó. Đây là một số tình huống thường gặp khi bạn nên sử dụng Decorator design pattern:

1. **Mở rộng chức năng của một đối tượng mà không ảnh hưởng đến các đối tượng khác:** Decorator cho phép bạn thêm chức
   năng mới vào một đối tượng cụ thể mà không cần thay đổi các đối tượng khác trong hệ thống.
2. **Khi bạn có nhiều tùy chọn chức năng có thể kết hợp:** Decorator cho phép bạn xây dựng các kết hợp chức năng động
   bằng cách thêm hoặc loại bỏ các decorator khác nhau.
3. **Khi bạn muốn tránh sử dụng class con quá nhiều:** Sử dụng class con để mở rộng chức năng có thể dẫn đến sự tăng
   cường của số lượng class con, điều này có thể trở nên phức tạp và khó bảo trì. Decorator giúp tránh điều này.
4. **Khi bạn muốn mở rộng chức năng của các đối tượng tại thời điểm chạy:** Decorator cho phép bạn thêm hoặc bỏ bất kỳ
   decorator nào tại thời điểm chạy, do đó bạn có sự linh hoạt lớn hơn trong việc quản lý chức năng.
5. **Khi bạn muốn tách biệt việc quản lý chức năng mở rộng và đối tượng cơ bản:** Decorator cho phép bạn duy trì sự rõ
   ràng giữa chức năng mở rộng và đối tượng gốc, giúp code dễ đọc và dễ bảo trì hơn.

## Running

```
python main.py
python example.py
```