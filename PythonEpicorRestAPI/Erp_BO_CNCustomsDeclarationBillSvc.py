import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CNCustomsDeclarationBillSvc
# Description: CustomsDeclarationBill
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclarationBills(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNCustomsDeclarationBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsDeclarationBills
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills",headers=creds) as resp:
           return await resp.json()

async def post_CNCustomsDeclarationBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsDeclarationBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclarationBills_Company_DeclarationBill(Company, DeclarationBill, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNCustomsDeclarationBill item
   Description: Calls GetByID to retrieve the CNCustomsDeclarationBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsDeclarationBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNCustomsDeclarationBills_Company_DeclarationBill(Company, DeclarationBill, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNCustomsDeclarationBill for the service
   Description: Calls UpdateExt to update CNCustomsDeclarationBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsDeclarationBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNCustomsDeclarationBills_Company_DeclarationBill(Company, DeclarationBill, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNCustomsDeclarationBill item
   Description: Call UpdateExt to delete CNCustomsDeclarationBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsDeclarationBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")",headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclarationBillDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNCustomsDeclarationBillDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsDeclarationBillDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails",headers=creds) as resp:
           return await resp.json()

async def post_CNCustomsDeclarationBillDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsDeclarationBillDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNCustomsDeclarationBillDetail item
   Description: Calls GetByID to retrieve the CNCustomsDeclarationBillDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsDeclarationBillDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNCustomsDeclarationBillDetail for the service
   Description: Calls UpdateExt to update CNCustomsDeclarationBillDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsDeclarationBillDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNCustomsDeclarationBillDetail item
   Description: Call UpdateExt to delete CNCustomsDeclarationBillDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsDeclarationBillDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillHdrLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCNCustomsDeclarationBillHeader, whereClauseCNCustomsDeclarationBillDetail, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCNCustomsDeclarationBillHeader=" + whereClauseCNCustomsDeclarationBillHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCNCustomsDeclarationBillDetail=" + whereClauseCNCustomsDeclarationBillDetail
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(declarationBill, epicorHeaders = None):
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
   params += "declarationBill=" + declarationBill

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: Performs validations
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCNWeightUOMClass(epicorHeaders = None):
   """  
   Summary: Invoke method GetCNWeightUOMClass
   Description: Returns XbSyst.CNWeightUOMClass. This method is only used by Smart Client.
   OperationID: GetCNWeightUOMClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCNWeightUOMClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeSourceDocumentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSourceDocumentType
   Description: Performs validations and sets defaults values after the Source Document Type has been changed
   OperationID: ChangeSourceDocumentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSourceDocumentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSourceDocumentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustVendorNum
   Description: Performs validations and sets defaults values after the Customer/Supplier has been changed
   OperationID: ChangeCustVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoice
   Description: Sets the default values after changing the invoice
   OperationID: ChangeInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Performs validations and sets defaults values after the Part has been changed
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyCode
   Description: Performs validations and sets defaults values after the Currency has been changed
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteDeclarationBillHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteDeclarationBillHeader
   Description: Deletes DeclarationBillHeader.
   OperationID: DeleteDeclarationBillHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDeclarationBillHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDeclarationBillHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNCustomsDeclarationBillHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNCustomsDeclarationBillHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsDeclarationBillHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsDeclarationBillHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsDeclarationBillHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNCustomsDeclarationBillDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNCustomsDeclarationBillDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsDeclarationBillDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsDeclarationBillDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsDeclarationBillDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsDeclarationBillDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsDeclarationBillHeaderRow] = obj["value"]
      pass

class Erp_Tablesets_CNCustomsDeclarationBillDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.TradeMode:str = obj["TradeMode"]
      """  Trade Mode  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.TradePort:str = obj["TradePort"]
      """  Trade Port  """  
      self.Agent:str = obj["Agent"]
      """  Agent  """  
      self.NetWeight:int = obj["NetWeight"]
      """  Net Weight  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.SourceDocumentType:str = obj["SourceDocumentType"]
      """  Source Document Type  """  
      self.CustVendorNum:int = obj["CustVendorNum"]
      """  Customer/Supplier Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.APInvNum:str = obj["APInvNum"]
      """  AP Invoice Num  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DeclarationAmt:int = obj["DeclarationAmt"]
      """  Declaration Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.DspCurrencyID:str = obj["DspCurrencyID"]
      self.DspDirection:str = obj["DspDirection"]
      self.DspInvoiceCurrencyID:str = obj["DspInvoiceCurrencyID"]
      self.DspInvoiceNum:str = obj["DspInvoiceNum"]
      self.DspSourceDocumentType:str = obj["DspSourceDocumentType"]
      self.DspTradeMode:str = obj["DspTradeMode"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceDeleted:bool = obj["InvoiceDeleted"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclarationBillHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.TradeMode:str = obj["TradeMode"]
      """  Trade Mode  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.TradePort:str = obj["TradePort"]
      """  Trade Port  """  
      self.Agent:str = obj["Agent"]
      """  Agent  """  
      self.NetWeight:int = obj["NetWeight"]
      """  Net Weight  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.SourceDocumentType:str = obj["SourceDocumentType"]
      """  Source Document Type  """  
      self.CustVendorNum:int = obj["CustVendorNum"]
      """  Customer/Supplier Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.APInvNum:str = obj["APInvNum"]
      """  AP Invoice Num  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DeclarationAmt:int = obj["DeclarationAmt"]
      """  Declaration Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceCurrencyCode:str = obj["InvoiceCurrencyCode"]
      self.InvoiceDeleted:bool = obj["InvoiceDeleted"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.DspCurrencyID:str = obj["DspCurrencyID"]
      self.DspDirection:str = obj["DspDirection"]
      self.DspInvoiceCurrencyID:str = obj["DspInvoiceCurrencyID"]
      self.DspInvoiceNum:str = obj["DspInvoiceNum"]
      self.DspSourceDocumentType:str = obj["DspSourceDocumentType"]
      self.DspTradeMode:str = obj["DspTradeMode"]
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCurrencyCode_input:
   """ Required : 
   currencyCode
   ds
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustVendorNum_input:
   """ Required : 
   custVendorNum
   ds
   """  
   def __init__(self, obj):
      self.custVendorNum:int = obj["custVendorNum"]
      """  new value  """  
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class ChangeCustVendorNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoice_input:
   """ Required : 
   invoiceNum
   apInvNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.apInvNum:str = obj["apInvNum"]
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class ChangeInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  new value  """  
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSourceDocumentType_input:
   """ Required : 
   documentType
   ds
   """  
   def __init__(self, obj):
      self.documentType:str = obj["documentType"]
      """  new value  """  
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class ChangeSourceDocumentType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   declarationBill
   """  
   def __init__(self, obj):
      self.declarationBill:str = obj["declarationBill"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteDeclarationBillHeader_input:
   """ Required : 
   ds
   updateReferencedDoc
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      self.updateReferencedDoc:bool = obj["updateReferencedDoc"]
      """  if true then DeclarationBill field of ShipHead, RcvHead, RMAHead, DMRHead will be cleared and DeclarationBillHeader will be deleted, else warning message will be returned  """  
      pass

class DeleteDeclarationBillHeader_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CNCustomsDeclarationBillDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.TradeMode:str = obj["TradeMode"]
      """  Trade Mode  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.TradePort:str = obj["TradePort"]
      """  Trade Port  """  
      self.Agent:str = obj["Agent"]
      """  Agent  """  
      self.NetWeight:int = obj["NetWeight"]
      """  Net Weight  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.SourceDocumentType:str = obj["SourceDocumentType"]
      """  Source Document Type  """  
      self.CustVendorNum:int = obj["CustVendorNum"]
      """  Customer/Supplier Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.APInvNum:str = obj["APInvNum"]
      """  AP Invoice Num  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DeclarationAmt:int = obj["DeclarationAmt"]
      """  Declaration Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.DspCurrencyID:str = obj["DspCurrencyID"]
      self.DspDirection:str = obj["DspDirection"]
      self.DspInvoiceCurrencyID:str = obj["DspInvoiceCurrencyID"]
      self.DspInvoiceNum:str = obj["DspInvoiceNum"]
      self.DspSourceDocumentType:str = obj["DspSourceDocumentType"]
      self.DspTradeMode:str = obj["DspTradeMode"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceDeleted:bool = obj["InvoiceDeleted"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclarationBillHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.HandbookCode:str = obj["HandbookCode"]
      """  Handbook Code  """  
      self.TradeMode:str = obj["TradeMode"]
      """  Trade Mode  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date  """  
      self.ContractNumber:str = obj["ContractNumber"]
      """  Contract Number  """  
      self.TradePort:str = obj["TradePort"]
      """  Trade Port  """  
      self.Agent:str = obj["Agent"]
      """  Agent  """  
      self.NetWeight:int = obj["NetWeight"]
      """  Net Weight  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.SourceDocumentType:str = obj["SourceDocumentType"]
      """  Source Document Type  """  
      self.CustVendorNum:int = obj["CustVendorNum"]
      """  Customer/Supplier Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  AR Invoice Number  """  
      self.APInvNum:str = obj["APInvNum"]
      """  AP Invoice Num  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DeclarationAmt:int = obj["DeclarationAmt"]
      """  Declaration Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceCurrencyCode:str = obj["InvoiceCurrencyCode"]
      self.InvoiceDeleted:bool = obj["InvoiceDeleted"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.DspCurrencyID:str = obj["DspCurrencyID"]
      self.DspDirection:str = obj["DspDirection"]
      self.DspInvoiceCurrencyID:str = obj["DspInvoiceCurrencyID"]
      self.DspInvoiceNum:str = obj["DspInvoiceNum"]
      self.DspSourceDocumentType:str = obj["DspSourceDocumentType"]
      self.DspTradeMode:str = obj["DspTradeMode"]
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclarationBillListTableset:
   def __init__(self, obj):
      self.CNCustomsDeclarationBillHdrLst:list[Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow] = obj["CNCustomsDeclarationBillHdrLst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNCustomsDeclarationBillTableset:
   def __init__(self, obj):
      self.CNCustomsDeclarationBillHeader:list[Erp_Tablesets_CNCustomsDeclarationBillHeaderRow] = obj["CNCustomsDeclarationBillHeader"]
      self.CNCustomsDeclarationBillDetail:list[Erp_Tablesets_CNCustomsDeclarationBillDetailRow] = obj["CNCustomsDeclarationBillDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset:
   def __init__(self, obj):
      self.CNCustomsDeclarationBillHeader:list[Erp_Tablesets_CNCustomsDeclarationBillHeaderRow] = obj["CNCustomsDeclarationBillHeader"]
      self.CNCustomsDeclarationBillDetail:list[Erp_Tablesets_CNCustomsDeclarationBillDetailRow] = obj["CNCustomsDeclarationBillDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   declarationBill
   """  
   def __init__(self, obj):
      self.declarationBill:str = obj["declarationBill"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
      pass

class GetCNWeightUOMClass_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCNCustomsDeclarationBillDetail_input:
   """ Required : 
   ds
   declarationBill
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      self.declarationBill:str = obj["declarationBill"]
      pass

class GetNewCNCustomsDeclarationBillDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCNCustomsDeclarationBillHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class GetNewCNCustomsDeclarationBillHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCNCustomsDeclarationBillHeader
   whereClauseCNCustomsDeclarationBillDetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCNCustomsDeclarationBillHeader:str = obj["whereClauseCNCustomsDeclarationBillHeader"]
      self.whereClauseCNCustomsDeclarationBillDetail:str = obj["whereClauseCNCustomsDeclarationBillDetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["returnObj"]
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

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      self.warnings:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclarationBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

