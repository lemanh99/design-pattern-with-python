## Source

https://refactoring.guru/design-patterns/command

## Cốt lõi:

> Command là một mẫu thiết kế hành vi (behavioral design pattern) chuyển đổi một yêu cầu thành một đối tượng độc lập
> chứa toàn bộ thông tin về yêu cầu. Sự biến đổi này cho phép bạn truyền các yêu cầu dưới dạng đối số của phương thức,
> hoãn hoặc đưa yêu cầu vào hàng đợi để thực thi, và hỗ trợ các thao tác có khả năng hoàn tác.

## Structure

![alt tag](command.png)

Các bước tạo command chính:

1. **Xác định các thành phần chính:**

- Client: Đây là đối tượng gửi yêu cầu.
- Receiver: Đây là đối tượng thực hiện các hành động thực tế.
- Command: Đây là interface hoặc lớp trừu tượng đại diện cho các yêu cầu. Nó phải có một phương thức để thực hiện yêu
  cầu (thường được gọi là execute()).

2. **Tạo các lớp cụ thể của Command:** Định nghĩa các lớp cụ thể của Command, mỗi lớp đại diện cho một loại yêu cầu cụ
   thể. Mỗi lớp này cần triển khai phương thức execute() để thực hiện yêu cầu.
3. **Kết nối Command với Receiver:** Command cần biết đối tượng Receiver mà nó sẽ gửi yêu cầu đến. Điều này có thể được
   thực hiện thông qua việc truyền đối tượng Receiver vào Command thông qua constructor hoặc setter method.
4. **Tạo và cấu hình Client:** Tạo đối tượng Client và cấu hình nó để gửi các yêu cầu tới các đối tượng Command cụ thể.
5. **Thực thi yêu cầu:** Khi Client muốn gửi yêu cầu, nó sẽ tạo một đối tượng Command tương ứng và gửi nó tới
   CommandInvoker (nếu có), sau đó CommandInvoker sẽ gửi yêu cầu tới Receiver để thực hiện.
6. **(Optional) Tạo CommandInvoker:** CommandInvoker là một lớp trung gian tùy chọn giữa Client và Command. Nó giúp quản
   lý hàng đợi các yêu cầu, lập lịch thực thi chúng hoặc thực hiện các thao tác khác liên quan đến việc điều khiển yêu
   cầu.
7. **Hỗ trợ Undo và Redo (tuỳ chọn):** Để hỗ trợ undo và redo, bạn cần cung cấp cơ chế lưu trữ trạng thái hoặc thay đổi
   để có thể hoàn tác và làm lại các yêu cầu.

## Description

### Mục đích

1. **Tách biệt người gửi yêu cầu (client) và người thực hiện yêu cầu (receiver):** Pattern này giúp tạo ra một lớp trung
   gian (command) để giữ thông tin về một yêu cầu cụ thể và biểu diễn nó dưới dạng một đối tượng độc lập. Điều này giúp
   người gửi yêu cầu không cần biết đối tượng cụ thể nào sẽ thực hiện yêu cầu và cho phép dễ dàng thay đổi hoặc mở rộng
   các yêu cầu mà không làm thay đổi mã nguồn của client hoặc receiver.
2. **Hỗ trợ undo và redo:** Command pattern cho phép bạn lưu trữ các trạng thái hoặc thay đổi được thực hiện bởi các yêu
   cầu và cung cấp cách thực hiện các thao tác undo (hoàn tác) và redo (làm lại). Điều này làm cho việc quản lý trạng
   thái của ứng dụng trở nên dễ dàng.
3. **Quản lý lịch sử yêu cầu:** Bằng cách lưu trữ các đối tượng Command đã thực hiện, bạn có thể xây dựng một lịch sử
   các yêu cầu đã được thực hiện trong ứng dụng. Điều này có ích khi bạn muốn xem lại hoặc kiểm tra các yêu cầu trước đó
   hoặc khi cần lưu trữ dữ liệu audit.
4. **Hỗ trợ thực thi đồng thời (concurrency):** Command pattern có thể giúp quản lý và thực thi các yêu cầu đồng thời từ
   nhiều luồng hoặc tiến trình khác nhau, mà không gây xung đột hoặc lỗi.
5. **Sử dụng cho các tính năng thời gian chạy (runtime features):** Khi bạn muốn cấu hình hoặc điều khiển các yêu cầu
   trong thời gian chạy của ứng dụng mà không cần sửa đổi mã nguồn của ứng dụng.
6. **Tạo các macro commands:** Command pattern cho phép bạn tạo các đối tượng Command phức tạp bằng cách kết hợp nhiều
   yêu cầu đơn giản lại với nhau thành một đối tượng lớn hơn để thực hiện các thao tác phức tạp.

## Khi nào thì sử dụng command

Command design pattern được sử dụng khi bạn muốn tách biệt người gửi yêu cầu (client) và người thực hiện yêu cầu (
receiver) trong một ứng dụng. Pattern này giúp bạn biến các yêu cầu thành các đối tượng độc lập, có thể thực thi bất kỳ
lúc nào, giúp bạn linh hoạt quản lý các yêu cầu, sử dụng lịch sử yêu cầu, hoặc thực hiện các thao tác undo/redo. Dưới
đây là những tình huống thường gặp khi nên sử dụng Command design pattern:

1. **Yêu cầu đối với đối tượng gọi không biết cụ thể đối tượng thực hiện công việc:** Khi client muốn gửi yêu cầu tới
   một đối tượng, nhưng không biết chính xác đối tượng đó là gì hoặc không muốn phụ thuộc vào đối tượng cụ thể đó.
2. **Hỗ trợ undo và redo:** Command pattern cho phép bạn lưu trữ trạng thái trước đó của ứng dụng, từ đó bạn có thể dễ
   dàng thực hiện các thao tác undo (hoàn tác) và redo (làm lại).
3. **Quản lý lịch sử yêu cầu:** Bằng cách lưu trữ các đối tượng Command đã thực hiện, bạn có thể xây dựng một lịch sử
   các yêu cầu và duyệt qua chúng hoặc thậm chí lưu trữ chúng vào một hệ thống nhật ký.
4. **Hỗ trợ thực thi đồng thời (concurrency):** Command pattern có thể giúp quản lý và thực thi các yêu cầu đồng thời từ
   nhiều luồng hoặc tiến trình khác nhau.
5. **Sử dụng cho các tính năng thời gian chạy (runtime features):** Khi bạn muốn cấu hình hoặc điều khiển các yêu cầu
   trong thời gian chạy của ứng dụng.
6. **Tạo các macro commands:** Command pattern cho phép bạn tạo các đối tượng Command phức tạp bằng cách kết hợp nhiều
   yêu cầu đơn giản lại với nhau thành một đối tượng lớn hơn.

## Running

```
python main.py
python example.py
```