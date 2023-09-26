## Source

https://refactoring.guru/design-patterns/chain-of-responsibility

## Cốt lõi:

> Chain of Responsibility là một mẫu thiết kế hành vi cho phép bạn truyền các yêu cầu theo một chuỗi các xử lý. Khi nhận
> được một yêu cầu, mỗi xử lý quyết định xem có xử lý yêu cầu đó hay chuyển tiếp nó cho xử lý tiếp theo trong chuỗi.

## Structure

![alt tag](chain-of-responsibility.png)

Các bước tạo chain of responsibility chính:

1. **Xác định các handlers (xử lý):** Bạn cần xác định tất cả các handlers mà bạn muốn thêm vào chain. Mỗi handler sẽ
   thực hiện một phần cụ thể của xử lý yêu cầu.
2. **Tạo interface hoặc base class cho các handlers (tùy chọn):** Điều này giúp định rõ giao diện hoặc các phương thức
   cơ bản mà tất cả các handlers trong chain phải triển khai. Nếu tất cả các handlers có cấu trúc tương tự, bạn có thể
   sử dụng một giao diện hoặc lớp cơ sở để đơn giản hóa việc triển khai.
3. **Xây dựng các handlers cụ thể:** Tạo các lớp cụ thể cho từng handler và triển khai các phương thức cần thiết.
4. **Liên kết các handlers thành một chain:** Mỗi handler trong chain nên có một tham chiếu đến handler tiếp theo hoặc
   một cách để xác định handler tiếp theo trong chain. Cách này cho phép yêu cầu được truyền qua các handler theo một
   trình tự cụ thể.
5. **Xử lý yêu cầu:** Gửi yêu cầu đến handler đầu tiên trong chain. Handler này sẽ xem xét yêu cầu và quyết định xem nó
   có xử lý yêu cầu đó hay không. Nếu nó xử lý, quá trình kết thúc. Nếu không, nó sẽ truyền yêu cầu cho handler tiếp
   theo trong chain.
6. **Lặp lại quy trình cho đến khi yêu cầu được xử lý hoặc không còn handler nào để xử lý.**

## Description

### Mục đích

1. **Loại bỏ sự kết nối cứng giữa sender (người gửi yêu cầu) và receiver (người xử lý yêu cầu):** COR cho phép bạn xác
   định nhiều người xử lý cho một yêu cầu và cho phép bạn thay đổi cấu trúc của chain mà không làm thay đổi sender hoặc
   receiver. Điều này giúp tạo ra một sự linh hoạt lớn trong quá trình xử lý yêu cầu.
2. **Phân tách và tái sử dụng code:** Mẫu thiết kế COR giúp phân chia xử lý yêu cầu thành các handler nhỏ hơn, mỗi
   handler đảm nhận một nhiệm vụ cụ thể. Điều này tạo điều kiện thuận lợi cho tái sử dụng code, vì bạn có thể sử dụng
   các handler đã tồn tại để xử lý các yêu cầu khác mà có cùng cấu trúc.
3. **Thực hiện nguyên tắc "Single Responsibility":** COR giúp bạn áp dụng nguyên tắc "Single Responsibility" trong việc
   thiết kế code. Mỗi handler chỉ chịu trách nhiệm cho một khía cạnh cụ thể của xử lý yêu cầu, giúp code trở nên dễ đọc,
   dễ bảo trì và dễ mở rộng.
4. **Tạo ra một cơ chế xử lý yêu cầu tùy ý:** COR cho phép bạn thêm hoặc loại bỏ handler trong chain một cách dễ dàng.
   Điều này có nghĩa là bạn có thể linh hoạt thay đổi cách xử lý yêu cầu tùy theo nhu cầu mà không cần thay đổi code của
   sender hoặc receiver.
5. **Giảm sự phụ thuộc giữa các thành phần của hệ thống:** Chain of Responsibility giúp giảm sự phụ thuộc giữa các thành
   phần của hệ thống. Sender không cần biết ai sẽ xử lý yêu cầu của nó, và receiver cũng không cần biết ai gửi yêu cầu
   đến. Điều này tạo ra một sự độc lập và dễ dàng bảo trì trong hệ thống.

## Khi nào thì sử dụng chain of responsibility

Design pattern Chain of Responsibility (COR) được sử dụng trong các tình huống sau:

1. Khi bạn có một loạt các đối tượng xử lý hoặc handlers và bạn muốn cho phép một yêu cầu hoặc sự kiện được chuyển tiếp
   qua tất cả các handlers một cách tuần tự cho đến khi nó được xử lý hoặc không có handlers nào xử lý nó.
2. Khi bạn muốn tránh sự ràng buộc cứng giữa sender (người gửi yêu cầu) và receiver (người xử lý yêu cầu). Pattern này
   cho phép bạn thay đổi cấu trúc của handler chain mà không ảnh hưởng đến sender hoặc receiver.
3. Khi bạn muốn thể hiện nguyên tắc "single responsibility" bằng cách chia nhỏ các xử lý riêng biệt thành các handlers
   riêng lẻ, mỗi handler chịu trách nhiệm cho một khía cạnh cụ thể của xử lý yêu cầu.
4. Khi bạn muốn cung cấp một cơ hội cho các handlers thay đổi xử lý một cách linh hoạt. Bạn có thể thêm, loại bỏ hoặc
   thay đổi thứ tự của các handlers một cách dễ dàng mà không ảnh hưởng đến code của sender.
5. Khi bạn muốn có khả năng xử lý yêu cầu tùy theo tình huống. Mỗi handler có thể quyết định xem họ có thể xử lý yêu cầu
   hay không, và có thể thực hiện xử lý riêng biệt dựa trên điều kiện.

## Running

```
python main.py
python example.py
```