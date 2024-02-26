function state_space_represent()
    % Parámetros del sistema
    A = [0 1; -1 -1];
    B = [1; 0];
    C = [1 0];
    D = 0;

    % Condiciones iniciales
    x0 = [0; 0];

    % Tiempo de simulación
    tspan = [0 10];

    % Solucionar la ecuación diferencial
    [t, x] = ode45(@(t, x) system_dynamics(t, x, A, B), tspan, x0);

    % Obtener la salida y
    y = C*x' + D;

    % Graficar
    figure;
    plot(t, y);
    xlabel('Time (s)');
    ylabel('y(t)');
    title('Response of the System');
    grid on;
end

function dx = system_dynamics(t, x, A, B)
    u = sin(t);       % u(t) = sen(t)
    du_dt = cos(t);   % Derivada de u(t)

    dx = A*x + B*u + B*du_dt; % Usando la entrada y su derivada
end
