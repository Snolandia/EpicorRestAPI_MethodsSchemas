import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CNCustomsHandbookSvc
# Description: CN Customs Handbook Service
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsHandbooks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNCustomsHandbooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsHandbooks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsHandbookHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbooks",headers=creds) as resp:
           return await resp.json()

async def post_CNCustomsHandbooks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsHandbooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbooks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsHandbooks_Company_HandbookCode(Company, HandbookCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNCustomsHandbook item
   Description: Calls GetByID to retrieve the CNCustomsHandbook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsHandbook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbooks(" + Company + "," + HandbookCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNCustomsHandbooks_Company_HandbookCode(Company, HandbookCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNCustomsHandbook for the service
   Description: Calls UpdateExt to update CNCustomsHandbook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsHandbook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbooks(" + Company + "," + HandbookCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNCustomsHandbooks_Company_HandbookCode(Company, HandbookCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNCustomsHandbook item
   Description: Call UpdateExt to delete CNCustomsHandbook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsHandbook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbooks(" + Company + "," + HandbookCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsHandbookDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNCustomsHandbookDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsHandbookDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsHandbookDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbookDetails",headers=creds) as resp:
           return await resp.json()

async def post_CNCustomsHandbookDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsHandbookDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbookDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsHandbookDetails_Company_HandbookCode_HandbookLine(Company, HandbookCode, HandbookLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNCustomsHandbookDetail item
   Description: Calls GetByID to retrieve the CNCustomsHandbookDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsHandbookDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param HandbookLine: Desc: HandbookLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbookDetails(" + Company + "," + HandbookCode + "," + HandbookLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNCustomsHandbookDetails_Company_HandbookCode_HandbookLine(Company, HandbookCode, HandbookLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNCustomsHandbookDetail for the service
   Description: Calls UpdateExt to update CNCustomsHandbookDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsHandbookDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param HandbookLine: Desc: HandbookLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsHandbookDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbookDetails(" + Company + "," + HandbookCode + "," + HandbookLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNCustomsHandbookDetails_Company_HandbookCode_HandbookLine(Company, HandbookCode, HandbookLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNCustomsHandbookDetail item
   Description: Call UpdateExt to delete CNCustomsHandbookDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsHandbookDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HandbookCode: Desc: HandbookCode   Required: True   Allow empty value : True
      :param HandbookLine: Desc: HandbookLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/CNCustomsHandbookDetails(" + Company + "," + HandbookCode + "," + HandbookLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsHandbookHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCNCustomsHandbookHeader, whereClauseCNCustomsHandbookDetail, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCNCustomsHandbookHeader=" + whereClauseCNCustomsHandbookHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCNCustomsHandbookDetail=" + whereClauseCNCustomsHandbookDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(handbookCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "handbookCode=" + handbookCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveMtlLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveMtlLines
   Description: Retrieves Customs Handbook Material Lines
   OperationID: RetrieveMtlLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveMtlLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveMtlLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFinishedGoods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFinishedGoods
   Description: Performs validations and set defaults values after the finished goods has been changed
   OperationID: ChangeFinishedGoods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFinishedGoods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFinishedGoods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCustomsHandbook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCustomsHandbook
   Description: Updates CustomsHandbook with checking finished goods for duplicate
   OperationID: UpdateCustomsHandbook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCustomsHandbook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustomsHandbook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNCustomsHandbookHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNCustomsHandbookHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsHandbookHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsHandbookHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsHandbookHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNCustomsHandbookDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNCustomsHandbookDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsHandbookDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsHandbookDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsHandbookDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsHandbookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsHandbookDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsHandbookDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsHandbookHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsHandbookHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsHandbookHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsHandbookHeaderRow] = obj["value"]
      pass

class Erp_Tablesets_CNCustomsHandbookDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.HandbookLine:int = obj["HandbookLine"]
      """  Handbook Line  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  Finished Goods Number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Num  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CustomsItemNum:str = obj["CustomsItemNum"]
      """  Customs Item Number  """  
      self.RegistryQuantity:int = obj["RegistryQuantity"]
      """  Registry Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  ProcessMfgID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date  """  
      self.Closed:bool = obj["Closed"]
      """  Closed  """  
      self.CloseDate:str = obj["CloseDate"]
      """  Close Date  """  
      self.Deposit:int = obj["Deposit"]
      """  Deposit  """  
      self.GuaranteeAmt:int = obj["GuaranteeAmt"]
      """  Guarantee Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.PlanAllocationRate:int = obj["PlanAllocationRate"]
      """  Plan Allocation Rate  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date  """  
      self.Closed:bool = obj["Closed"]
      """  Closed  """  
      self.CloseDate:str = obj["CloseDate"]
      """  Close Date  """  
      self.Deposit:int = obj["Deposit"]
      """  Deposit  """  
      self.GuaranteeAmt:int = obj["GuaranteeAmt"]
      """  Guarantee Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.PlanAllocationRate:int = obj["PlanAllocationRate"]
      """  Plan Allocation Rate  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFinishedGoods_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

class ChangeFinishedGoods_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   handbookCode
   """  
   def __init__(self, obj):
      self.handbookCode:str = obj["handbookCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CNCustomsHandbookDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.HandbookLine:int = obj["HandbookLine"]
      """  Handbook Line  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  Finished Goods Number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Num  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CustomsItemNum:str = obj["CustomsItemNum"]
      """  Customs Item Number  """  
      self.RegistryQuantity:int = obj["RegistryQuantity"]
      """  Registry Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  ProcessMfgID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date  """  
      self.Closed:bool = obj["Closed"]
      """  Closed  """  
      self.CloseDate:str = obj["CloseDate"]
      """  Close Date  """  
      self.Deposit:int = obj["Deposit"]
      """  Deposit  """  
      self.GuaranteeAmt:int = obj["GuaranteeAmt"]
      """  Guarantee Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.PlanAllocationRate:int = obj["PlanAllocationRate"]
      """  Plan Allocation Rate  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookHeaderListTableset:
   def __init__(self, obj):
      self.CNCustomsHandbookHeaderList:list[Erp_Tablesets_CNCustomsHandbookHeaderListRow] = obj["CNCustomsHandbookHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNCustomsHandbookHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date  """  
      self.Closed:bool = obj["Closed"]
      """  Closed  """  
      self.CloseDate:str = obj["CloseDate"]
      """  Close Date  """  
      self.Deposit:int = obj["Deposit"]
      """  Deposit  """  
      self.GuaranteeAmt:int = obj["GuaranteeAmt"]
      """  Guarantee Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.PlanAllocationRate:int = obj["PlanAllocationRate"]
      """  Plan Allocation Rate  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookMtlLineRow:
   def __init__(self, obj):
      self.AttritionRate:int = obj["AttritionRate"]
      """  Attrition Rate  """  
      self.Company:str = obj["Company"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  Consumed Quantity  """  
      self.CustomsUOMCode:str = obj["CustomsUOMCode"]
      """  current part in BOM, China tab  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.HandbookLine:int = obj["HandbookLine"]
      """  Handbook Line  """  
      self.MtlSequenceNum:int = obj["MtlSequenceNum"]
      """  Material Sequence Number  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RegistryQty:int = obj["RegistryQty"]
      """  Registry Quantity  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity  """  
      self.UOMCode:str = obj["UOMCode"]
      """  current part in BOM, Materials Detail  """  
      self.Bonded:bool = obj["Bonded"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsHandbookMtlTableset:
   def __init__(self, obj):
      self.CNCustomsHandbookMtlLine:list[Erp_Tablesets_CNCustomsHandbookMtlLineRow] = obj["CNCustomsHandbookMtlLine"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNCustomsHandbookTableset:
   def __init__(self, obj):
      self.CNCustomsHandbookHeader:list[Erp_Tablesets_CNCustomsHandbookHeaderRow] = obj["CNCustomsHandbookHeader"]
      self.CNCustomsHandbookDetail:list[Erp_Tablesets_CNCustomsHandbookDetailRow] = obj["CNCustomsHandbookDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCNCustomsHandbookTableset:
   def __init__(self, obj):
      self.CNCustomsHandbookHeader:list[Erp_Tablesets_CNCustomsHandbookHeaderRow] = obj["CNCustomsHandbookHeader"]
      self.CNCustomsHandbookDetail:list[Erp_Tablesets_CNCustomsHandbookDetailRow] = obj["CNCustomsHandbookDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   handbookCode
   """  
   def __init__(self, obj):
      self.handbookCode:str = obj["handbookCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookHeaderListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCNCustomsHandbookDetail_input:
   """ Required : 
   ds
   handbookCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      self.handbookCode:str = obj["handbookCode"]
      pass

class GetNewCNCustomsHandbookDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCNCustomsHandbookHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

class GetNewCNCustomsHandbookHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCNCustomsHandbookHeader
   whereClauseCNCustomsHandbookDetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCNCustomsHandbookHeader:str = obj["whereClauseCNCustomsHandbookHeader"]
      self.whereClauseCNCustomsHandbookDetail:str = obj["whereClauseCNCustomsHandbookDetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class RetrieveMtlLines_input:
   """ Required : 
   handbookCode
   handbookLine
   """  
   def __init__(self, obj):
      self.handbookCode:str = obj["handbookCode"]
      """  Handbook Code  """  
      self.handbookLine:int = obj["handbookLine"]
      """  Handbook Line  """  
      pass

class RetrieveMtlLines_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsHandbookMtlTableset] = obj["returnObj"]
      pass

class UpdateCustomsHandbook_input:
   """ Required : 
   ds
   checkDuplicateFinishedGoods
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      self.checkDuplicateFinishedGoods:bool = obj["checkDuplicateFinishedGoods"]
      """  if true then duplicate is not allowed and if a duplicate exists the a Duplicate is true, otherwise isDuplicate is always false  """  
      pass

class UpdateCustomsHandbook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      self.handbookCode:str = obj["parameters"]
      self.handbookLine:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsHandbookTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsHandbookTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsHandbookTableset] = obj["ds"]
      pass

      """  output parameters  """  

