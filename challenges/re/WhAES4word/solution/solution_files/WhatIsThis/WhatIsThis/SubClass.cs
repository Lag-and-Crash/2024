using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WhatIsThis
{
    class SubClass : SuperClass
    {
        private List<Byte> kee = new List<Byte>
            { 0x54, 0x68, 0x69, 0x73, 0x49, 0x73, 0x41, 0x4C, 0x65, 0x65, 0x74, 0x4B, 0x65, 0x79, 0x21, 0x21 };
        public ulong What(int x)
        {
            var y = 0;
            while (x + y == y + x + x)
            {
                y++;
                x++;
                y++;
                x++;
                y++;
                What(x);
            }

            return 12345;
        }
        public SubClass() : base() { }
        public override int Funct1()
        {
            string h = "";
            List<char> c = new List<char> { 'a', 'b', 'c', '!', '1', '2' };
            foreach (char x in c)
            {
                h += x;
            }
            return base.Return0(h);
        }

        public override SuperClass Whatisthis()
        {
            SubClass x = new SubClass();
            x.doubl = 1;
            x.What(1);
            x.What(Convert.ToInt32(Convert.ToDouble(123456789)));
            return this;
        }

        public override string Part1OfFlag(int yy)
        {
            return "b";
        }

        public int veryembmethod(int x, int y, int z, int xyz)
        {
            if (x == y && y == z && z == xyz)
            {
                return 1;
            }
            else if (x ==11)
            {
                return 22;
            }
            else if (y == 987)
            {
                return 2222;
            }
            else
            {
                return 100000;
            }
        }

        public string theb(int x)
        {
            return x + "c";
        }
    }
}
