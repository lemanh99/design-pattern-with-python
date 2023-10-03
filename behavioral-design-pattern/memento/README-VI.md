## Source

https://refactoring.guru/design-patterns/memento

## Cốt lõi:

> Memento là một mẫu thiết kế hành vi cho phép bạn lưu và khôi phục trạng thái trước đó của một đối tượng mà không tiết
> lộ chi tiết về cách thức triển khai của nó.

## Structure

![alt tag](memento.png)

Các bước tạo memento chính:

1. **Xác định đối tượng gốc (Originator):** Đây là đối tượng mà bạn muốn lưu trạng thái của nó và khôi phục lại sau này.
   Đối
   tượng gốc phải có một phương thức để tạo Memento và một phương thức để khôi phục trạng thái từ Memento.
2. **Tạo Memento (Memento):** Định nghĩa một lớp Memento để lưu trạng thái của đối tượng gốc. Lớp Memento này cần có các
   thuộc tính để lưu trữ trạng thái và một cách để truy cập trạng thái đó (thường thông qua các phương thức get).
3. **Xác định quản lý trạng thái (Caretaker):** Quản lý trạng thái là đối tượng chịu trách nhiệm lưu trữ và quản lý các
   Memento. Nó có thể là một lớp riêng biệt hoặc một phần của đối tượng gốc, tùy thuộc vào thiết kế.
4. **Lưu trạng thái (Save State):** Khi bạn muốn lưu trạng thái của đối tượng gốc, bạn tạo một đối tượng Memento và
   truyền
   trạng thái hiện tại của đối tượng gốc vào Memento này.
5. **Lưu Memento vào quản lý trạng thái (Caretaker):** Sau khi bạn đã tạo Memento, bạn cần lưu trữ nó vào đối tượng quản
   lý
   trạng thái (Caretaker). Quản lý trạng thái sẽ quản lý danh sách các Memento.
6. **Khôi phục trạng thái (Restore State):** Khi bạn muốn khôi phục lại trạng thái của đối tượng gốc, bạn truy cập
   Memento
   tương ứng từ quản lý trạng thái và sử dụng nó để khôi phục trạng thái của đối tượng gốc.

## Description

### Mục đích

1. **Lưu trạng thái của một đối tượng:** Memento cho phép bạn lưu trữ trạng thái hiện tại của một đối tượng một cách độc
   lập
   với đối tượng đó. Điều này làm cho trạng thái của đối tượng không bị phụ thuộc vào cấu trúc hoặc triển khai của nó.
2. **Khôi phục lại trạng thái:** Memento cho phép bạn khôi phục lại trạng thái của đối tượng từ một lưu trữ trạng thái
   trước
   đó. Điều này hữu ích khi bạn muốn hoàn tác (undo) các thay đổi hoặc khôi phục lại trạng thái trước đó của đối tượng.
3. **Bảo vệ tính bao đóng (encapsulation):** Memento pattern giúp duy trì tính bao đóng của đối tượng bằng cách ẩn trạng
   thái và cung cấp một cách tiếp cận chỉ qua giao diện của Memento. Điều này giúp đảm bảo rằng trạng thái của đối tượng
   không thể bị truy cập hoặc sửa đổi trực tiếp từ bên ngoài.
4. **Quản lý lịch sử hoặc trạng thái:** Memento pattern cung cấp khả năng quản lý và duyệt lịch sử hoặc trạng thái của
   một
   đối tượng. Điều này hữu ích khi bạn muốn theo dõi các thay đổi đã xảy ra hoặc cần tạo các chức năng như hoàn tác và
   làm lại trong ứng dụng.

## Khi nào thì sử dụng memento

Memento design pattern (mẫu thiết kế Memento) là một trong các mẫu thiết kế trong lập trình hướng đối tượng. Mẫu thiết
kế này được sử dụng khi bạn muốn lưu trạng thái của một đối tượng và khôi phục lại trạng thái đó sau này mà không tiết
lộ chi tiết triển khai trạng thái đó. Memento pattern giúp bạn quản lý và lưu trữ lịch sử hoặc trạng thái của một đối
tượng một cách an toàn.
Dưới đây là một số tình huống phù hợp để sử dụng Memento pattern:

1. **Giao diện hoàn tác (Undo/Redo):** Khi bạn muốn thực hiện chức năng hoàn tác (undo) và làm lại (redo) trong ứng dụng
   của
   mình, bạn có thể sử dụng Memento để lưu trạng thái của đối tượng trước mỗi thay đổi và sau đó khôi phục lại trạng
   thái đó khi người dùng yêu cầu hoàn tác hoặc làm lại.
2. **Lưu trạng thái của ứng dụng:** Trong trường hợp bạn muốn lưu trạng thái của ứng dụng để khôi phục sau khi ứng dụng
   bị
   đóng, bạn có thể sử dụng Memento để lưu các trạng thái quan trọng của các đối tượng trong ứng dụng.
3. **Quản lý lịch sử trạng thái:** Đôi khi, bạn cần theo dõi và quản lý lịch sử trạng thái của một đối tượng để xem
   những
   thay đổi nào đã xảy ra. Memento pattern có thể được sử dụng để lưu trữ các phiên bản trạng thái trước đó của đối
   tượng.
4. **Sao lưu và khôi phục dữ liệu:** Trong các ứng dụng như trình soạn thảo văn bản hoặc trình duyệt web, bạn có thể sử
   dụng
   Memento để sao lưu và khôi phục dữ liệu người dùng đã nhập.

## Running

```
python main.py
python example.py
```