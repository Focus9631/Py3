parametr= 100;
random_pic = randi(255,parametr,"double");%Созданик картинки
for i=1:parametr
    Sinus (1:parametr, i) = random_pic (1:parametr, i).*sin(pi*i/(parametr/2));%Наша синусойда
end
[x]=random_pic;
[y]=random_pic;
z=sqrt(x.^2+y.^2);
c=z>15;
figure(1);%Вывод графика
imshow(Sinus,[ ]);%
s1=sum(Sinus,1)/parametr;%Сумма всех столбцов измененного изображения
s5=sum(random_pic,1)/parametr;
figure(2);%Вывод графика
grid minor; hold on;
plot(abs(s1));
Fur=fftshift(fft(s1));%Преобразование Фурье
FurFilter=Fur.*c;
% Fur((parametr/10):parametr-((parametr/10)+(parametr/100)))=0;%Удаление высоких частот
s2=ifft(FurFilter);%Обратное преобразование Фурье
plot(abs(s2));%Вывод графика
plot(Sinus(:,8));%
Srednee1 = mean(s5);%Среднее значение нашего входящего изображения
Srednee2 = mean(abs(s2));%Среднее значение нашего измененного изображения
D4=var(Sinus);
D1=var(s5);
D2=var(s2);
D3=D2/D1;
limit= 1;
if D3 > limit
    disp('Картинка не взвешенная')
else
    disp('Картинка взвешенная')
end
% figure(3);%Вывод графика
% plot(V); grid minor; hold on;
% plot(s2);
% figure(2);
% plot(abs(Fur));