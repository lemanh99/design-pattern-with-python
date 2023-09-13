## Source

https://refactoring.guru/design-patterns/singleton

## Cốt lõi:

> Singleton là một mẫu thiết kế sáng tạo cho phép bạn đảm bảo rằng một lớp chỉ có một instance duy nhất, đồng thời cung
> cấp một point truy cập toàn cục đến instance này

## Structure

![alt tag](singleton.png)

Các bước tạo singleton pattern chính:

1. **Tạo một base class hoặc interface:** Đầu tiên, bạn cần tạo một base class hoặc interface mà các class Singleton sẽ
   kế thừa hoặc triển khai. Lớp này thường chứa một biến tĩnh để lưu trữ instance duy nhất và một phương thức tĩnh để
   truy cập instance đó.

2. **Định nghĩa biến tĩnh để lưu trữ instance duy nhất:** Trong base class, bạn cần định nghĩa một static variable để
   lưu trữ instance duy nhất của class. Biến này sẽ được sử dụng để kiểm tra xem instance đã được tạo chưa.

3. **Tạo một phương thức tĩnh để truy cập instance duy nhất:** Trong base class, bạn cần định nghĩa một phương thức tĩnh
   để cung cấp truy cập toàn cục đến instance duy nhất. Phương thức này sẽ kiểm tra xem instance đã được tạo chưa và trả
   về instance hiện có hoặc tạo một instance mới nếu chưa tồn tại.

4. **Đảm bảo rằng việc tạo instance chỉ diễn ra một lần:** Trong phương thức tạo instance, bạn cần đảm bảo rằng việc tạo
   instance chỉ diễn ra một lần, để đảm bảo tính duy nhất của instance. Điều này có thể thực hiện thông qua cơ chế
   khóa (lock) hoặc kiểm tra tạo instance trong các điều kiện đồng thời (thread-safe conditions).

5. **Triển khai các lớp Singleton:** Bây giờ, bạn có thể triển khai các lớp Singleton cụ thể bằng cách kế thừa base
   class hoặc triển khai interface. Trong subclass, bạn không cần triển khai lại biến tĩnh hoặc phương thức tĩnh, vì
   chúng đã được định nghĩa trong base class.

## Description

### Mục đích

1. **Đảm bảo sự duy nhất:** Singleton đảm bảo rằng chỉ có một instance duy nhất của lớp được tạo ra trong suốt vòng đời
   của
   ứng dụng. Điều này hữu ích khi bạn muốn giới hạn việc tạo nhiều instance của một lớp để tránh xung đột và lãng phí
   tài nguyên.
2. **Truy cập toàn cục:** Singleton cung cấp một point truy cập toàn cục đến instance của nó. Điều này cho phép các phần
   khác của ứng dụng dễ dàng truy cập và sử dụng thể hiện đó mà không cần biết cụ thể về cách instance được tạo ra hoặc
   quản lý.
3. **Giảm tải hệ thống:** Singleton giúp giảm tải hệ thống bằng cách đảm bảo rằng chỉ có một thể hiện của một lớp được
   tạo
   ra và sử dụng trong suốt thời gian chạy của ứng dụng. Điều này đặc biệt hữu ích khi tạo instance của các tài nguyên
   đắt đỏ như kết nối cơ sở dữ liệu hoặc bản sao lớp quản lý cấu hình.
4. **Bảo vệ trạng thái chia sẻ:** Singleton giúp bảo vệ trạng thái chia sẻ giữa các thành phần khác nhau của ứng dụng.
   Bằng
   cách sử dụng instance duy nhất, bạn đảm bảo rằng không có xung đột dữ liệu xảy ra khi các thành phần cố gắng truy cập
   hoặc thay đổi trạng thái chung.
5. **Khắc phục sự nhầm lẫn:** Singleton giúp loại bỏ sự nhầm lẫn khi tạo instance của lớp. Khi chỉ có một instance duy
   nhất,
   bạn loại bỏ khả năng tạo instance mới vô tình và giúp dễ dàng theo dõi và duyệt mã.
6. **Tối ưu hóa việc sử dụng tài nguyên:** Singleton có thể được sử dụng để tạo và quản lý các tài nguyên chia sẻ như
   pool
   kết nối, bản sao đối tượng cấu hình, bộ nhớ cache, và nhiều tài nguyên khác mà bạn muốn tối ưu hóa việc sử dụng.

Tóm lại, Singleton giúp kiểm soát việc tạo instance và cung cấp truy cập toàn cục đến instance duy nhất của một lớp,
đồng thời giúp quản lý và tối ưu hóa sử dụng tài nguyên trong ứng dụng.

## Khi nào thì sử dụng singleton pattern

Singleton Pattern được sử dụng trong các tình huống mà bạn muốn đảm bảo rằng một lớp chỉ có một instance duy nhất và bạn
cần cung cấp một cách truy cập toàn cục đến instance đó. Dưới đây là một số tình huống thường gặp khi bạn nên sử dụng
Singleton Pattern:

1. Kết nối cơ sở dữ liệu: Khi bạn cần duy trì một kết nối đến cơ sở dữ liệu trong toàn bộ ứng dụng, Singleton Pattern
   giúp đảm bảo rằng chỉ có một kết nối cơ sở dữ liệu duy nhất được sử dụng và tránh tạo nhiều kết nối không cần thiết.
2. Cấu hình ứng dụng: Singleton Pattern có thể được sử dụng để lưu trữ và cung cấp cấu hình ứng dụng (ví dụ: thông tin
   kết nối cơ sở dữ liệu, cài đặt khóa, cấu hình giao diện người dùng).
3. Quản lý tài nguyên chia sẻ: Khi bạn cần quản lý tài nguyên chia sẻ như pool kết nối, bộ nhớ cache, hoặc các tài
   nguyên có chi phí tạo mới cao, Singleton giúp tối ưu hóa việc sử dụng tài nguyên này.
4. Đối tượng điều khiển ứng dụng: Singleton Pattern có thể được sử dụng để đại diện cho đối tượng điều khiển ứng dụng (
   application controller) để quản lý luồng xử lý chính của ứng dụng.
5. Ghi log hoặc theo dõi hoạt động ứng dụng: Singleton Pattern có thể được sử dụng để ghi log hoặc theo dõi các hoạt
   động quan trọng trong ứng dụng.
6. Cửa sổ đối tượng (Window Manager): Trong các ứng dụng đồ họa, Singleton Pattern có thể được sử dụng để quản lý cửa sổ
   đối tượng và đảm bảo rằng chỉ có một cửa sổ đối tượng hoặc cửa sổ chính được sử dụng.
7. Service Locator Pattern: Trong trường hợp sử dụng Service Locator Pattern để tìm và cung cấp các dịch vụ (services)
   trong ứng dụng, Singleton Pattern có thể được sử dụng để triển khai Service Locator.
8. Cơ chế bảo mật hoặc kiểm tra quyền truy cập: Singleton Pattern có thể được sử dụng để duy trì các đối tượng chịu
   trách nhiệm kiểm tra quyền truy cập hoặc bảo mật trong ứng dụng.

Tóm lại, bạn nên sử dụng Singleton Pattern khi bạn muốn đảm bảo rằng một lớp chỉ có một instance duy nhất và bạn cần
cung cấp một cách truy cập toàn cục đến instance đó trong toàn bộ ứng dụng. Tuy nhiên, hãy cân nhắc sử dụng nó một cách
cẩn thận và đảm bảo rằng nó thực sự phù hợp với yêu cầu của ứng dụng của bạn, vì nó có thể làm cho mã trở nên khó kiểm
tra và phụ thuộc quá mức vào một đối tượng duy nhất.

## Running

```
python main.py
python example.py
```