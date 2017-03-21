#ifndef _QXU_BUF
#define _QXU_BUF

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
		printf("buffer created\n");
	};

	~CBuff(){
		if (m_pBuf)
		{
			free(m_pBuf);
			m_pBuf = NULL;
		}

		m_nBufSize = 0;
		m_posi = 0;
		printf("buffer released\n");
	};

	bool Resize(int size)
	{
		if (size <= 0)
		{
			return false;
		}

		m_nBufSize = size;
		m_pBuf = (char*)realloc(m_pBuf, size);
		if (m_pBuf == NULL)
		{
			printf("realloc failed\n");
			return false;
		}

		return true;
	}

	int Append2Buff(const char* src, int nBytes)
	{
		if (!src || nBytes <= 0)
		{
			return 0;
		}

		if (m_nBufSize - 1 < nBytes + m_posi)
		{
			if (Resize(nBytes + m_posi + 1) == false)
			{
				return 0;
			}

			m_nBufSize = nBytes + m_posi + 1;
		}

		memcpy(m_pBuf + m_posi, src, nBytes);
		m_posi += nBytes;

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

	void ResetPosi()
	{
		m_posi = 0;
	}

	bool SetPosi(int posi)
	{
		if (posi > m_nBufSize)
		{
			return false;
		}
		
		m_posi = posi;
		return true;
	}

	bool SetValueAtPosi(int posi, char val)
	{
		if (posi > m_nBufSize - 1)
		{
			return false;
		}
		
		m_pBuf[posi] = val;
		return true;
	}
};
#endif