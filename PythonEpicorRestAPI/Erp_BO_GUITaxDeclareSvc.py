import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GUITaxDeclareSvc
# Description: Tax Declaration Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GUITaxDeclares(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GUITaxDeclares items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GUITaxDeclares
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUITaxDeclareRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares",headers=creds) as resp:
           return await resp.json()

async def post_GUITaxDeclares(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GUITaxDeclares
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company, DeclareYear, DeclarePeriod, GUISource, GUIFormatCode, TranDocType, InvoiceNum, LegalNumber, GUITaxTypeCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GUITaxDeclare item
   Description: Calls GetByID to retrieve the GUITaxDeclare item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GUITaxDeclare
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclareYear: Desc: DeclareYear   Required: True
      :param DeclarePeriod: Desc: DeclarePeriod   Required: True
      :param GUISource: Desc: GUISource   Required: True   Allow empty value : True
      :param GUIFormatCode: Desc: GUIFormatCode   Required: True   Allow empty value : True
      :param TranDocType: Desc: TranDocType   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
      :param GUITaxTypeCode: Desc: GUITaxTypeCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company, DeclareYear, DeclarePeriod, GUISource, GUIFormatCode, TranDocType, InvoiceNum, LegalNumber, GUITaxTypeCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GUITaxDeclare for the service
   Description: Calls UpdateExt to update GUITaxDeclare. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GUITaxDeclare
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclareYear: Desc: DeclareYear   Required: True
      :param DeclarePeriod: Desc: DeclarePeriod   Required: True
      :param GUISource: Desc: GUISource   Required: True   Allow empty value : True
      :param GUIFormatCode: Desc: GUIFormatCode   Required: True   Allow empty value : True
      :param TranDocType: Desc: TranDocType   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
      :param GUITaxTypeCode: Desc: GUITaxTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company, DeclareYear, DeclarePeriod, GUISource, GUIFormatCode, TranDocType, InvoiceNum, LegalNumber, GUITaxTypeCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GUITaxDeclare item
   Description: Call UpdateExt to delete GUITaxDeclare item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GUITaxDeclare
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclareYear: Desc: DeclareYear   Required: True
      :param DeclarePeriod: Desc: DeclarePeriod   Required: True
      :param GUISource: Desc: GUISource   Required: True   Allow empty value : True
      :param GUIFormatCode: Desc: GUIFormatCode   Required: True   Allow empty value : True
      :param TranDocType: Desc: TranDocType   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
      :param GUITaxTypeCode: Desc: GUITaxTypeCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUITaxDeclareListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGUITaxDeclare, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseGUITaxDeclare=" + whereClauseGUITaxDeclare
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(declareYear, declarePeriod, guISource, guIFormatCode, tranDocType, invoiceNum, legalNumber, guITaxTypeCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "declareYear=" + declareYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "declarePeriod=" + declarePeriod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "guISource=" + guISource
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "guIFormatCode=" + guIFormatCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranDocType=" + tranDocType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "legalNumber=" + legalNumber
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "guITaxTypeCode=" + guITaxTypeCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranDocTypeID
   Description: Method to call when changing the Transaction Document Type.
   OperationID: ChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UserIsTaxDeclarationAdmin(epicorHeaders = None):
   """  
   Summary: Invoke method UserIsTaxDeclarationAdmin
   Description: Check if Current User is in Tax Declaration Admin Security Group
   OperationID: UserIsTaxDeclarationAdmin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserIsTaxDeclarationAdmin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CalcAmountIncludeTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcAmountIncludeTax
   Description: This method should be called to calculate include amount tax.
   OperationID: CalcAmountIncludeTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAmountIncludeTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAmountIncludeTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGUITaxDeclareFromExisting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGUITaxDeclareFromExisting
   Description: Create new row using existing one as source (after adjusting the source row key field values
   OperationID: GetNewGUITaxDeclareFromExisting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUITaxDeclareFromExisting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUITaxDeclareFromExisting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSourceRecordsChain(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSourceRecordsChain
   Description: Retrieve the chain of source records
   OperationID: GetSourceRecordsChain
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceRecordsChain_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceRecordsChain_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGUITaxDeclare(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGUITaxDeclare
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGUITaxDeclare
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUITaxDeclare_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUITaxDeclare_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GUITaxDeclareListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GUITaxDeclareRow] = obj["value"]
      pass

class Erp_Tablesets_GUITaxDeclareListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclareYear:int = obj["DeclareYear"]
      """  DeclareYear  """  
      self.DeclarePeriod:int = obj["DeclarePeriod"]
      """  DeclarePeriod  """  
      self.GUISource:str = obj["GUISource"]
      """  GUISource  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  GUIFormatCode  """  
      self.TranDocType:str = obj["TranDocType"]
      """  TranDocType  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  GUITaxTypeCode  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxInPrice:bool = obj["TaxInPrice"]
      """  TaxInPrice  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ExportBillNum:str = obj["ExportBillNum"]
      """  ExportBillNum  """  
      self.ExportBillType:str = obj["ExportBillType"]
      """  ExportBillType  """  
      self.ExportMark:str = obj["ExportMark"]
      """  ExportMark  """  
      self.ExportType:str = obj["ExportType"]
      """  ExportType  """  
      self.ImportTaxBasis:int = obj["ImportTaxBasis"]
      """  ImportTaxBasis  """  
      self.ImportTaxAmt:int = obj["ImportTaxAmt"]
      """  ImportTaxAmt  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  GUIDeductCode  """  
      self.SellerGUICode:str = obj["SellerGUICode"]
      """  SellerGUICode  """  
      self.BuyerGUICode:str = obj["BuyerGUICode"]
      """  BuyerGUICode  """  
      self.AmtExclTax:int = obj["AmtExclTax"]
      """  AmtExclTax  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ManualInsert:bool = obj["ManualInsert"]
      """  ManualInsert  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.GUIGroup:str = obj["GUIGroup"]
      """  GUIGroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUITaxDeclareRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclareYear:int = obj["DeclareYear"]
      """  DeclareYear  """  
      self.DeclarePeriod:int = obj["DeclarePeriod"]
      """  DeclarePeriod  """  
      self.GUISource:str = obj["GUISource"]
      """  GUISource  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  GUIFormatCode  """  
      self.TranDocType:str = obj["TranDocType"]
      """  TranDocType  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  GUITaxTypeCode  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxInPrice:bool = obj["TaxInPrice"]
      """  TaxInPrice  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ExportBillNum:str = obj["ExportBillNum"]
      """  ExportBillNum  """  
      self.ExportBillType:str = obj["ExportBillType"]
      """  ExportBillType  """  
      self.ExportMark:str = obj["ExportMark"]
      """  ExportMark  """  
      self.ExportType:str = obj["ExportType"]
      """  ExportType  """  
      self.ImportTaxBasis:int = obj["ImportTaxBasis"]
      """  ImportTaxBasis  """  
      self.ImportTaxAmt:int = obj["ImportTaxAmt"]
      """  ImportTaxAmt  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  GUIDeductCode  """  
      self.SellerGUICode:str = obj["SellerGUICode"]
      """  SellerGUICode  """  
      self.BuyerGUICode:str = obj["BuyerGUICode"]
      """  BuyerGUICode  """  
      self.AmtExclTax:int = obj["AmtExclTax"]
      """  AmtExclTax  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ManualInsert:bool = obj["ManualInsert"]
      """  ManualInsert  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.GUIGroup:str = obj["GUIGroup"]
      """  GUIGroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  SourceSysRowID  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcAmountIncludeTax_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

class CalcAmountIncludeTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranDocTypeID_input:
   """ Required : 
   TranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type.  """  
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

class ChangeTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   declareYear
   declarePeriod
   guISource
   guIFormatCode
   tranDocType
   invoiceNum
   legalNumber
   guITaxTypeCode
   """  
   def __init__(self, obj):
      self.declareYear:int = obj["declareYear"]
      self.declarePeriod:int = obj["declarePeriod"]
      self.guISource:str = obj["guISource"]
      self.guIFormatCode:str = obj["guIFormatCode"]
      self.tranDocType:str = obj["tranDocType"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.legalNumber:str = obj["legalNumber"]
      self.guITaxTypeCode:str = obj["guITaxTypeCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GUITaxDeclareListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclareYear:int = obj["DeclareYear"]
      """  DeclareYear  """  
      self.DeclarePeriod:int = obj["DeclarePeriod"]
      """  DeclarePeriod  """  
      self.GUISource:str = obj["GUISource"]
      """  GUISource  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  GUIFormatCode  """  
      self.TranDocType:str = obj["TranDocType"]
      """  TranDocType  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  GUITaxTypeCode  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxInPrice:bool = obj["TaxInPrice"]
      """  TaxInPrice  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ExportBillNum:str = obj["ExportBillNum"]
      """  ExportBillNum  """  
      self.ExportBillType:str = obj["ExportBillType"]
      """  ExportBillType  """  
      self.ExportMark:str = obj["ExportMark"]
      """  ExportMark  """  
      self.ExportType:str = obj["ExportType"]
      """  ExportType  """  
      self.ImportTaxBasis:int = obj["ImportTaxBasis"]
      """  ImportTaxBasis  """  
      self.ImportTaxAmt:int = obj["ImportTaxAmt"]
      """  ImportTaxAmt  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  GUIDeductCode  """  
      self.SellerGUICode:str = obj["SellerGUICode"]
      """  SellerGUICode  """  
      self.BuyerGUICode:str = obj["BuyerGUICode"]
      """  BuyerGUICode  """  
      self.AmtExclTax:int = obj["AmtExclTax"]
      """  AmtExclTax  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ManualInsert:bool = obj["ManualInsert"]
      """  ManualInsert  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.GUIGroup:str = obj["GUIGroup"]
      """  GUIGroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUITaxDeclareListTableset:
   def __init__(self, obj):
      self.GUITaxDeclareList:list[Erp_Tablesets_GUITaxDeclareListRow] = obj["GUITaxDeclareList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GUITaxDeclareRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclareYear:int = obj["DeclareYear"]
      """  DeclareYear  """  
      self.DeclarePeriod:int = obj["DeclarePeriod"]
      """  DeclarePeriod  """  
      self.GUISource:str = obj["GUISource"]
      """  GUISource  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  GUIFormatCode  """  
      self.TranDocType:str = obj["TranDocType"]
      """  TranDocType  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  GUITaxTypeCode  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxInPrice:bool = obj["TaxInPrice"]
      """  TaxInPrice  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ExportBillNum:str = obj["ExportBillNum"]
      """  ExportBillNum  """  
      self.ExportBillType:str = obj["ExportBillType"]
      """  ExportBillType  """  
      self.ExportMark:str = obj["ExportMark"]
      """  ExportMark  """  
      self.ExportType:str = obj["ExportType"]
      """  ExportType  """  
      self.ImportTaxBasis:int = obj["ImportTaxBasis"]
      """  ImportTaxBasis  """  
      self.ImportTaxAmt:int = obj["ImportTaxAmt"]
      """  ImportTaxAmt  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  GUIDeductCode  """  
      self.SellerGUICode:str = obj["SellerGUICode"]
      """  SellerGUICode  """  
      self.BuyerGUICode:str = obj["BuyerGUICode"]
      """  BuyerGUICode  """  
      self.AmtExclTax:int = obj["AmtExclTax"]
      """  AmtExclTax  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ManualInsert:bool = obj["ManualInsert"]
      """  ManualInsert  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.GUIGroup:str = obj["GUIGroup"]
      """  GUIGroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  SourceSysRowID  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUITaxDeclareSourceTableset:
   def __init__(self, obj):
      self.GUITaxDeclare:list[Erp_Tablesets_GUITaxDeclareRow] = obj["GUITaxDeclare"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GUITaxDeclareTableset:
   def __init__(self, obj):
      self.GUITaxDeclare:list[Erp_Tablesets_GUITaxDeclareRow] = obj["GUITaxDeclare"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGUITaxDeclareTableset:
   def __init__(self, obj):
      self.GUITaxDeclare:list[Erp_Tablesets_GUITaxDeclareRow] = obj["GUITaxDeclare"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   declareYear
   declarePeriod
   guISource
   guIFormatCode
   tranDocType
   invoiceNum
   legalNumber
   guITaxTypeCode
   """  
   def __init__(self, obj):
      self.declareYear:int = obj["declareYear"]
      self.declarePeriod:int = obj["declarePeriod"]
      self.guISource:str = obj["guISource"]
      self.guIFormatCode:str = obj["guIFormatCode"]
      self.tranDocType:str = obj["tranDocType"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.legalNumber:str = obj["legalNumber"]
      self.guITaxTypeCode:str = obj["guITaxTypeCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGUITaxDeclareFromExisting_input:
   """ Required : 
   sourceRecordSysRowID
   ds
   """  
   def __init__(self, obj):
      self.sourceRecordSysRowID:str = obj["sourceRecordSysRowID"]
      """  SysRowID of source record  """  
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

class GetNewGUITaxDeclareFromExisting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGUITaxDeclare_input:
   """ Required : 
   ds
   declareYear
   declarePeriod
   guISource
   guIFormatCode
   tranDocType
   invoiceNum
   legalNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      self.declareYear:int = obj["declareYear"]
      self.declarePeriod:int = obj["declarePeriod"]
      self.guISource:str = obj["guISource"]
      self.guIFormatCode:str = obj["guIFormatCode"]
      self.tranDocType:str = obj["tranDocType"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.legalNumber:str = obj["legalNumber"]
      pass

class GetNewGUITaxDeclare_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGUITaxDeclare
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGUITaxDeclare:str = obj["whereClauseGUITaxDeclare"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSourceRecordsChain_input:
   """ Required : 
   sourceRecordSysRowID
   """  
   def __init__(self, obj):
      self.sourceRecordSysRowID:str = obj["sourceRecordSysRowID"]
      """  Source Record ID for Current Record  """  
      pass

class GetSourceRecordsChain_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GUITaxDeclareSourceTableset] = obj["returnObj"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGUITaxDeclareTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGUITaxDeclareTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUITaxDeclareTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UserIsTaxDeclarationAdmin_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  User is in Tax Declaration Admin Security Group  """  
      pass

