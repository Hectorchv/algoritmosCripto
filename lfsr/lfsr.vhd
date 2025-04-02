library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity lfsr is
    Port (
        clk     : in  std_logic;
        reset   : in  std_logic;
        enable  : in  std_logic;
        lfsr_out: out std_logic_vector(7 downto 0);
		  sequence: out std_logic
    );
end lfsr;

architecture Behavioral of lfsr is
    signal lfsr_reg : std_logic_vector(7 downto 0) := "11000011";
	 signal sequence_reg : std_logic := '0';
begin
    process(clk, reset)
    begin
        if reset = '1' then
            lfsr_reg <= "11000011";
        elsif rising_edge(clk) then
            if enable = '1' then
				-- Polinomio primitivo: x^8 + x^6 + x^5 + x^4 + 1
					lfsr_reg <= (lfsr_reg(7) xor lfsr_reg(6) xor lfsr_reg(1) xor lfsr_reg(0) ) & lfsr_reg(7 downto 1);
					sequence_reg <= lfsr_reg(0);
            end if;
        end if;
    end process;

    lfsr_out <= lfsr_reg;
	 sequence <= sequence_reg;
	 
end Behavioral;
