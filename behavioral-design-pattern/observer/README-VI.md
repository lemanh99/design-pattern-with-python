## Source

https://refactoring.guru/design-patterns/observer

## Cốt lõi:

> Observer là một mẫu thiết kế hành vi cho phép bạn xác định một cơ chế đăng ký để thông báo cho nhiều đối tượng về bất
> kỳ sự kiện nào xảy ra đối với đối tượng mà họ đang quan sát.

## Structure

![alt tag](observer.png)

Các bước tạo observer chính:
Observer design pattern là một trong những mẫu thiết kế phổ biến trong lập trình. Nó được sử dụng khi bạn muốn theo dõi
và thông báo về sự thay đổi trong trạng thái của một đối tượng (subject) đến một tập hợp các đối tượng khác (observers)
mà không cần biết cụ thể là những observers đó là ai. Dưới đây là các bước để tạo Observer Design Pattern:

1. Xác định Subject:

- Đầu tiên, bạn cần xác định đối tượng mà bạn muốn theo dõi (subject). Đây là đối tượng sẽ chịu trách nhiệm thông báo
  cho các observers về các thay đổi trong trạng thái của nó.

2. Xác định Observer:

- Bạn cần xác định giao diện (interface) cho các observers. Giao diện này sẽ chứa các phương thức mà các observers cần
  triển khai để nhận thông báo từ subject khi có sự thay đổi.

3. Thêm danh sách Observers vào Subject:

- Trong subject, bạn cần có một danh sách (list hoặc mảng) để lưu trữ các observers đang theo dõi nó.

4. Thêm các phương thức để quản lý Observers:

- Subject cần cung cấp các phương thức để thêm, xoá và thông báo cho các observers. Ví dụ:
    - attach(Observer): Thêm một observer vào danh sách.
    - detach(Observer): Xoá một observer khỏi danh sách.
    - notify(): Thông báo cho tất cả các observers về sự thay đổi trong trạng thái của subject.

5. Cập nhật Observers:

- Trong các observers, bạn cần triển khai phương thức mà subject đã xác định trong giao diện observer. Phương thức này
  sẽ được gọi khi subject thông báo về sự thay đổi.

6. Tạo các đối tượng Subject và Observer:

- Tạo các đối tượng subject và observer cụ thể và kết nối chúng với nhau bằng cách sử dụng các phương thức attach().

7. Thực hiện sự thay đổi và thông báo:

- Khi trạng thái của subject thay đổi, subject cần gọi phương thức notify() để thông báo cho tất cả các observers về sự
  thay đổi. Các observers sẽ được thông báo và có thể xử lý sự thay đổi theo cách riêng của họ.

8. Kiểm tra kết quả:

- Kiểm tra xem các observers đã nhận và xử lý thông báo từ subject một cách chính xác hay không.

## Description

### Mục đích

1. **Tạo sự phụ thuộc lỏng lẻo giữa các đối tượng:** Pattern này cho phép bạn xây dựng các hệ thống có sự phụ thuộc giữa
   các đối tượng một cách lỏng lẻo. Subject không cần biết cụ thể là ai và có bao nhiêu observers, và observers không
   cần biết về sự tồn tại của nhau. Điều này làm cho hệ thống dễ mở rộng và duy trì.
2. **Thông báo về sự thay đổi:** Observer cho phép subject thông báo cho các observers về sự thay đổi trong trạng thái
   của nó một cách tự động. Khi trạng thái của subject thay đổi, tất cả các observers đã đăng ký sẽ được thông báo và có
   thể thực hiện các hành động tương ứng mà không cần phải kiểm tra liên tục.
3. **Phân tách logic:** Pattern này giúp phân tách logic xử lý sự kiện (event handling) ra khỏi đối tượng gốc. Thay vì
   đặt logic xử lý sự kiện trong đối tượng chính, bạn có thể tách nó ra thành các observers riêng biệt, làm cho mã nguồn
   dễ đọc hơn và dễ bảo trì hơn.
4. **Phân tách giao diện người dùng (UI) và logic:** Trong các ứng dụng đồ họa, Observer Pattern cho phép bạn phân tách
   UI và logic. Các thành phần UI (observers) có thể đăng ký để theo dõi sự thay đổi trong trạng thái của đối tượng (
   subject), mà không cần phải lẫn lộn với logic xử lý dữ liệu.
5. **Loại bỏ sự phụ thuộc đồng bộ (tight coupling):** Khi bạn sử dụng Observer Pattern, bạn giảm thiểu sự phụ thuộc đồng
   bộ giữa các đối tượng, giúp mã nguồn trở nên dễ bảo trì, mở rộng và tái sử dụng hơn.

## Khi nào thì sử dụng observer

Bạn nên sử dụng Observer Design Pattern khi bạn có một tình huống trong đó một đối tượng (subject) cần thông báo về sự
thay đổi trong trạng thái của nó đến một tập hợp các đối tượng khác (observers) mà bạn không biết cụ thể là những
observers đó là ai hoặc có thể có nhiều observers khác nhau muốn theo dõi subject.
Dưới đây là một số tình huống phổ biến mà bạn có thể sử dụng Observer Design Pattern:

1. **UI và Sự kiện trong ứng dụng đồ họa:** Khi bạn cần cập nhật giao diện người dùng (UI) một cách tự động khi trạng
   thái dữ liệu thay đổi, ví dụ như thông báo cho các thành phần UI về sự thay đổi trong dữ liệu.
2. **Trong các hệ thống ghi log:** Khi bạn muốn ghi log (log events hoặc thay đổi) và bạn muốn nhiều phần mềm khác nhau
   có thể đăng ký để ghi log khi có sự thay đổi.
3. **Quản lý sự kiện (Event Handling):** Khi bạn xây dựng các hệ thống xử lý sự kiện và muốn các đối tượng khác nhau có
   thể đăng ký (subscribe) và thực hiện xử lý khi sự kiện xảy ra.
4. **Thiết kế chơi game:** Trong việc xây dựng trò chơi, bạn có thể sử dụng Observer Pattern để theo dõi và xử lý sự
   kiện như va chạm, bắn đạn, hoặc thay đổi trạng thái của các nhân vật.
5. **Trong hệ thống đa luồng (multithreading):** Khi bạn muốn các luồng (threads) khác nhau theo dõi và phản ứng khi một
   luồng thực hiện một công việc cụ thể.
6. **Chương trình chat và thông báo realtime:** Trong các ứng dụng chat, bạn có thể sử dụng Observer để thông báo cho
   các người dùng khác khi có tin nhắn mới.
7. **Hệ thống tài chính và giao dịch:** Trong các hệ thống tài chính, bạn có thể sử dụng Observer để theo dõi các thay
   đổi giá cổ phiếu và thông báo cho các khách hàng hoặc nhà đầu tư.

## Running

```
python main.py
python example.py
```