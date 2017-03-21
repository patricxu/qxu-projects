#define BUF_SIZE 200
class CBuff{
private:
	char* m_pBuf;
	int m_nBufSize;
	int m_posi;//position into the buffer;

	CBuff(const CBuff&);
	CBuff& operator= (const CBuff&);

public:
	CBuff(){
		m_pBuf = (char*)malloc(BUF_SIZE);
		m_nBufSize = BUF_SIZE;
		m_posi = 0;
	};

	~CBuff(){
		if (m_pBuf)
		{
			free(m_pBuf);
			m_pBuf = NULL;
		}

		m_nBufSize = 0;
		m_posi = 0;
	};

	bool Resize(int size)
	{
		if (size <= 0)
		{
			return;
		}

		m_nBufSize = size;
		m_pBuf = (char*)realloc(m_pBuf, size);
		if (m_pBuf == NULL)
		{
			printf("realloc failed\n");
			return false;
		}
	}

	int Add2Buff(const char* src, int nBytes)
	{
		if (!src || nBytes <= 0)
		{
			return 0;
		}

		if (m_nBufSize < nBytes + m_posi)
		{
			if (Resize(nBytes + m_posi) == false)
			{
				return 0;
			}

			m_nBufSize = nBytes + m_posi;
		}

		memcpy(m_pBuf + m_posi, src, nBytes);
		return nBytes;
	}

	char* GetBuff()
	{
		return m_pBuf;
	}

	int GetBuffSize()
	{
		return m_nBufSize;
	}

	int GetBufPosi()
	{
		return m_posi;
	}
};
