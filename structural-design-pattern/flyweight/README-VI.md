## Source

https://refactoring.guru/design-patterns/flyweight

## Cốt lõi:

> Decorator là một mẫu thiết kế cấu trúc cho phép bạn đính kèm các hành vi mới vào các đối tượng bằng cách đặt những đối
> tượng này vào bên trong các đối tượng bọc đặc biệt chứa các hành vi.

## Structure

![alt tag](flyweight.png)

Các bước tạo một flyweight

1. Xác định dữ liệu chung: Đầu tiên, xác định những phần dữ liệu hoặc trạng thái mà các đối tượng Flyweight sẽ chia sẻ.
   Đây là những thông tin không thay đổi hoặc ít thay đổi trong quá trình thực thi của ứng dụng.
2. Tạo lớp Flyweight: Tạo một lớp Flyweight, đóng vai trò là đối tượng chia sẻ. Lớp này sẽ bao gồm các thuộc tính chứa
   thông tin chung và phương thức để truy cập hoặc cập nhật thông tin này.
3. Tạo lớp Flyweight Factory: Tạo một lớp Factory (nếu cần) để quản lý việc tạo và quản lý các đối tượng Flyweight.
   Factory sẽ kiểm tra xem một đối tượng Flyweight đã tồn tại chưa trước khi tạo mới nó và chia sẻ đối tượng đã có khi
   cần.
3. Tạo các đối tượng Flyweight: Tạo các đối tượng Flyweight bằng cách sử dụng lớp Factory (nếu có) hoặc tạo trực tiếp.
   Khi tạo các đối tượng này, hãy đảm bảo chia sẻ thông tin chung thay vì sao chép nó.
4. Sử dụng đối tượng Flyweight: Trong ứng dụng, sử dụng các đối tượng Flyweight khi cần tham chiếu đến thông tin chung
   đó. Thay vì tạo mới đối tượng Flyweight mỗi khi cần, bạn sẽ nhận được một thể hiện đã tồn tại hoặc mới được tạo nếu
   chưa tồn tại.
5. Quản lý trạng thái phi chia sẻ: Nếu có các trạng thái riêng biệt cho mỗi đối tượng Flyweight, đảm bảo rằng trạng thái
   này không được lưu trữ trong đối tượng Flyweight mà phải được quản lý bên ngoài. Trạng thái phi chia sẻ này sẽ được
   truyền vào đối tượng Flyweight khi cần.
6. Theo dõi sự thay đổi và tương tác: Theo dõi việc sử dụng và tương tác với các đối tượng Flyweight để đảm bảo tính
   nhất quán và an toàn trong ứng dụng.

## Description

### Mục đích

Mục đích chính của Flyweight Design Pattern là giảm thiểu sự sử dụng bộ nhớ hoặc tối ưu hóa hiệu suất bằng cách chia sẻ
tối đa dữ liệu hoặc trạng thái giữa các đối tượng. Pattern này thường được sử dụng trong trường hợp khi có rất nhiều đối
tượng có cùng một phần lớn dữ liệu chung hoặc có thể được chia sẻ. Flyweight giúp tiết kiệm bộ nhớ và tăng hiệu suất
bằng cách sử dụng một số đối tượng chia sẻ thay vì tạo mới một đối tượng riêng lẻ cho mỗi trường hợp.
Dưới đây là một số mục đích cụ thể của Flyweight Design Pattern:

1. **Tiết kiệm bộ nhớ:** Bằng cách chia sẻ thông tin chung giữa các đối tượng, Flyweight giúp giảm sự sử dụng bộ nhớ.
   Điều này quan trọng khi bạn có hàng ngàn đối tượng cùng sử dụng một tập dữ liệu lớn.
2. **Tối ưu hóa hiệu suất:** Flyweight giúp cải thiện hiệu suất bằng cách giảm thiểu việc tạo và hủy các đối tượng cùng
   loại. Nó giúp giảm tải cho máy chủ hoặc ứng dụng, đặc biệt khi có nhiều yêu cầu xử lý.
3. **Tạo đối tượng bất biến:** Flyweight có thể kết hợp với Flyweight Factory để đảm bảo rằng một đối tượng chỉ được tạo
   một lần và sau đó chia sẻ trong toàn bộ ứng dụng. Điều này có thể đảm bảo tính bất biến và an toàn trong ứng dụng.
4. **Tăng tái sử dụng:** Flyweight cho phép bạn tái sử dụng các đối tượng đã có thay vì tạo mới chúng. Điều này giúp
   giảm sự phức tạp của mã và tạo điều kiện thuận lợi cho việc bảo trì và mở rộng ứng dụng.
5. **Giảm thiểu tài nguyên hệ thống:** Nếu bạn có một ứng dụng hoặc hệ thống có nhiều đối tượng tương tự, sử dụng
   Flyweight có thể giúp giảm thiểu tài nguyên hệ thống và giúp ứng dụng chạy mượt mà hơn.

## Khi nào thì sử dụng flyweight

Flyweight Design Pattern thường được sử dụng trong các tình huống sau khi bạn nhận thấy rằng có nhiều đối tượng có chung
một số lượng lớn dữ liệu chung hoặc trạng thái, và bạn muốn tối ưu hóa việc sử dụng bộ nhớ hoặc hiệu suất bằng cách chia
sẻ thông tin này giữa các đối tượng. Dưới đây là một số tình huống cụ thể khi bạn nên xem xét sử dụng Flyweight:

1. **Sử dụng chung dữ liệu tĩnh:** Khi có một tập dữ liệu tĩnh (không thay đổi) mà nhiều đối tượng sử dụng, ví dụ như
   danh sách các biểu tượng hoặc loại sản phẩm, bạn có thể sử dụng Flyweight để chia sẻ dữ liệu này giữa các đối tượng.
2. **Ứng dụng đòi hỏi tối ưu hóa bộ nhớ:** Trong các ứng dụng có số lượng lớn đối tượng, việc tạo một đối tượng riêng lẻ
   cho mỗi trường hợp có thể dẫn đến sử dụng bộ nhớ lớn. Sử dụng Flyweight giúp giảm thiểu việc sử dụng bộ nhớ bằng cách
   chia sẻ thông tin chung.
3. **Cải thiện hiệu suất:** Khi ứng dụng của bạn đối diện với tình huống yêu cầu tối ưu hóa hiệu suất, như xử lý hàng
   ngàn yêu cầu mỗi giây, Flyweight có thể giúp giảm tải cho ứng dụng bằng cách giảm thiểu tạo mới đối tượng và giảm
   thiểu overhead.
4. **Tạo đối tượng không thay đổi (immutable):** Flyweight thường kết hợp tốt với việc tạo đối tượng không thay đổi. Nếu
   bạn muốn đảm bảo rằng một đối tượng không thay đổi chỉ được tạo một lần và sau đó chia sẻ trong toàn bộ ứng dụng,
   Flyweight có thể giúp thực hiện điều này.
5. **Ứng dụng có nhiều trạng thái:** Khi có một số trạng thái chia sẻ giữa các đối tượng, bạn có thể sử dụng Flyweight
   để chia sẻ trạng thái này thay vì lưu trữ nó trong từng đối tượng.
6. **Giảm tải cho máy chủ:** Trong ứng dụng máy chủ, ví dụ như máy chủ web hoặc máy chủ trò chơi, Flyweight có thể giúp
   giảm tải cho máy chủ bằng cách chia sẻ thông tin chung với nhiều yêu cầu từ khách hàng.
7. **Tối ưu hóa các tài nguyên hệ thống:** Khi bạn muốn giảm thiểu tài nguyên hệ thống mà ứng dụng của bạn sử dụng,
   Flyweight có thể là một lựa chọn hữu ích.

## Running

```
python main.py
python example.py
```