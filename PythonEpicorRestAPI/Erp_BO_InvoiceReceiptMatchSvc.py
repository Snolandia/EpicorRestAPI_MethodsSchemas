import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InvoiceReceiptMatchSvc
# Description: Invoice Receipt Match business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InvoiceReceiptMatches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvoiceReceiptMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvoiceReceiptMatches
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches",headers=creds) as resp:
           return await resp.json()

async def get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum(Company, InvoiceNum, InvoiceLine, PONum, POLine, PORelNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvoiceReceiptMatch item
   Description: Calls GetByID to retrieve the InvoiceReceiptMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvoiceReceiptMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvoiceMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum_APInvcRcptDtlMatches(Company, InvoiceNum, InvoiceLine, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APInvcRcptDtlMatches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APInvcRcptDtlMatches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvcRcptDtlMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")/APInvcRcptDtlMatches",headers=creds) as resp:
           return await resp.json()

async def get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum_APInvcRcptDtlMatches_Company_VendorNum_PurPoint_PackSlip_PackLine_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, PONum, POLine, PORelNum, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvcRcptDtlMatch item
   Description: Calls GetByID to retrieve the APInvcRcptDtlMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvcRcptDtlMatch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvcRcptDtlMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")/APInvcRcptDtlMatches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_APInvcRcptDtlMatches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APInvcRcptDtlMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvcRcptDtlMatches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvcRcptDtlMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/APInvcRcptDtlMatches",headers=creds) as resp:
           return await resp.json()

async def get_APInvcRcptDtlMatches_Company_VendorNum_PurPoint_PackSlip_PackLine_InvoiceNum_InvoiceLine(Company, VendorNum, PurPoint, PackSlip, PackLine, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvcRcptDtlMatch item
   Description: Calls GetByID to retrieve the APInvcRcptDtlMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvcRcptDtlMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvcRcptDtlMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/APInvcRcptDtlMatches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceMatchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: GetRows for Kinetic LandingPage
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(invoiceNum, invoiceLine, vendorNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: GetByID
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceLine=" + invoiceLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns the Data Schema records
   OperationID: Get_GetList
      :param whereClause: Desc: Where clause   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckGLInterfaceForPost(epicorHeaders = None):
   """  
   Summary: Invoke method CheckGLInterfaceForPost
   Description: Checks to see if GL interface is available before posting.  Is run before the
PostMatches method.  A question is returned to ask the user if they want to continue
with the post or not if the interface is not available.  If the answer is no, the
PostMatches method is not run.
   OperationID: CheckGLInterfaceForPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterfaceForPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetAPIRMtch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPIRMtch
   Description: Get the APIRMtch records.
   OperationID: GetAPIRMtch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPIRMtch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPIRMtch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvoiceReceiptMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvoiceReceiptMatch
   Description: Get the InvoiceReceipt records from the list dataset.
   OperationID: GetInvoiceReceiptMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoiceReceiptMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoiceReceiptMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSupplierXRefParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSupplierXRefParts
   Description: This method gets the XRef information for a given supplier part
   OperationID: GetSupplierXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplierXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplierXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchInvoiceReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchInvoiceReceipt
   Description: Match an invoice and a receipt.
   OperationID: MatchInvoiceReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchInvoiceReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchInvoiceReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostMatches(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostMatches
   Description: Post the Invoice/Receipt matches.
   OperationID: PostMatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostMatches_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostMatches_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSupplierXRefParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSupplierXRefParts
   Description: This method sets the XRef fields for a supplier part
   OperationID: SetSupplierXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSupplierXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSupplierXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnMatchInvoiceReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnMatchInvoiceReceipt
   Description: Unmatch an invoice and a receipt.
   OperationID: UnMatchInvoiceReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnMatchInvoiceReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnMatchInvoiceReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvcRcptDtlMatchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvoiceMatchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvoiceMatchRow] = obj["value"]
      pass

class Erp_Tablesets_APInvcRcptDtlMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.ReceiptDate:str = obj["ReceiptDate"]
      self.ReceiptVendorQty:int = obj["ReceiptVendorQty"]
      self.QuantitiesMatch:bool = obj["QuantitiesMatch"]
      self.ReceiptUnitCost:int = obj["ReceiptUnitCost"]
      self.VendorPart:str = obj["VendorPart"]
      self.Matched:bool = obj["Matched"]
      self.PartNum:str = obj["PartNum"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.ReceiptVendorUOM:str = obj["ReceiptVendorUOM"]
      """  Receipt Vendor Unit of Measure  """  
      self.ReceiptUnitCostUOM:str = obj["ReceiptUnitCostUOM"]
      """  Receipt Unit Cost Unit of Measure  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceMatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceVendorQty:int = obj["InvoiceVendorQty"]
      self.PartNum:str = obj["PartNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.VendorPartNum:str = obj["VendorPartNum"]
      self.UnitCost:int = obj["UnitCost"]
      self.ExtCost:int = obj["ExtCost"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.BaseUnitCost:int = obj["BaseUnitCost"]
      self.BaseExtCost:int = obj["BaseExtCost"]
      self.Currency:str = obj["Currency"]
      self.InvoiceVendorUOM:str = obj["InvoiceVendorUOM"]
      """  Invoice Vendor Unit of Measure  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceVendorQty:int = obj["InvoiceVendorQty"]
      self.PartNum:str = obj["PartNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.VendorPartNum:str = obj["VendorPartNum"]
      self.UnitCost:int = obj["UnitCost"]
      self.ExtCost:int = obj["ExtCost"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.BaseUnitCost:int = obj["BaseUnitCost"]
      self.BaseExtCost:int = obj["BaseExtCost"]
      self.Currency:str = obj["Currency"]
      self.InvoiceVendorUOM:str = obj["InvoiceVendorUOM"]
      """  Invoice Vendor Unit of Measure  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckGLInterfaceForPost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cContinuePostMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_APIRMtchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table.  InvoiceLine of the related APInvDtl.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  """  
      self.PackLine:int = obj["PackLine"]
      """  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvoiceVendorQty:int = obj["InvoiceVendorQty"]
      self.ReceiptVendorQty:int = obj["ReceiptVendorQty"]
      self.InvoiceUnitCost:int = obj["InvoiceUnitCost"]
      self.ReceiptUnitCost:int = obj["ReceiptUnitCost"]
      self.PartNum:str = obj["PartNum"]
      self.ReceiptVendorUOM:str = obj["ReceiptVendorUOM"]
      """  Receipt Vendor Unit of Measure  """  
      self.InvoiceVendorUOM:str = obj["InvoiceVendorUOM"]
      """  Invoice Vendor Unit of Measure  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APIRMtchTableset:
   def __init__(self, obj):
      self.APIRMtch:list[Erp_Tablesets_APIRMtchRow] = obj["APIRMtch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvcRcptDtlMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.ReceiptDate:str = obj["ReceiptDate"]
      self.ReceiptVendorQty:int = obj["ReceiptVendorQty"]
      self.QuantitiesMatch:bool = obj["QuantitiesMatch"]
      self.ReceiptUnitCost:int = obj["ReceiptUnitCost"]
      self.VendorPart:str = obj["VendorPart"]
      self.Matched:bool = obj["Matched"]
      self.PartNum:str = obj["PartNum"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.ReceiptVendorUOM:str = obj["ReceiptVendorUOM"]
      """  Receipt Vendor Unit of Measure  """  
      self.ReceiptUnitCostUOM:str = obj["ReceiptUnitCostUOM"]
      """  Receipt Unit Cost Unit of Measure  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceMatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceVendorQty:int = obj["InvoiceVendorQty"]
      self.PartNum:str = obj["PartNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.VendorPartNum:str = obj["VendorPartNum"]
      self.UnitCost:int = obj["UnitCost"]
      self.ExtCost:int = obj["ExtCost"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.BaseUnitCost:int = obj["BaseUnitCost"]
      self.BaseExtCost:int = obj["BaseExtCost"]
      self.Currency:str = obj["Currency"]
      self.InvoiceVendorUOM:str = obj["InvoiceVendorUOM"]
      """  Invoice Vendor Unit of Measure  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceMatchListTableset:
   def __init__(self, obj):
      self.APInvoiceMatchList:list[Erp_Tablesets_APInvoiceMatchListRow] = obj["APInvoiceMatchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvoiceMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.MatchedReference:str = obj["MatchedReference"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.InvoiceVendorQty:int = obj["InvoiceVendorQty"]
      self.PartNum:str = obj["PartNum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.VendorPartNum:str = obj["VendorPartNum"]
      self.UnitCost:int = obj["UnitCost"]
      self.ExtCost:int = obj["ExtCost"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.BaseUnitCost:int = obj["BaseUnitCost"]
      self.BaseExtCost:int = obj["BaseExtCost"]
      self.Currency:str = obj["Currency"]
      self.InvoiceVendorUOM:str = obj["InvoiceVendorUOM"]
      """  Invoice Vendor Unit of Measure  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvoiceReceiptMatchTableset:
   def __init__(self, obj):
      self.APInvoiceMatch:list[Erp_Tablesets_APInvoiceMatchRow] = obj["APInvoiceMatch"]
      self.APInvcRcptDtlMatch:list[Erp_Tablesets_APInvcRcptDtlMatchRow] = obj["APInvcRcptDtlMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefTableset:
   def __init__(self, obj):
      self.SupplierXRef:list[Erp_Tablesets_SupplierXRefRow] = obj["SupplierXRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPIRMtch_input:
   """ Required : 
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.pageSize:int = obj["pageSize"]
      """  The pageSize parameter  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage parameter  """  
      pass

class GetAPIRMtch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APIRMtchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   invoiceNum
   invoiceLine
   vendorNum
   """  
   def __init__(self, obj):
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["returnObj"]
      pass

class GetInvoiceReceiptMatch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceMatchListTableset] = obj["ds"]
      pass

class GetInvoiceReceiptMatch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceMatchListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvoiceMatchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSupplierXRefParts_input:
   """ Required : 
   partNum
   vendorNum
   poNum
   poLine
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Receipt Part Number  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Supplier Number  """  
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      self.poLine:int = obj["poLine"]
      """  PO Line  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  packing Slip  """  
      self.packLine:int = obj["packLine"]
      """  packing Line  """  
      pass

class GetSupplierXRefParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupplierXRefTableset] = obj["returnObj"]
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

class MatchInvoiceReceipt_input:
   """ Required : 
   cInvoiceNum
   iInvoiceLine
   iVendorNum
   cPurPoint
   cPackSlip
   iPackLine
   ds
   """  
   def __init__(self, obj):
      self.cInvoiceNum:str = obj["cInvoiceNum"]
      """  The Invoice Number of the APInvoiceMatch record  """  
      self.iInvoiceLine:int = obj["iInvoiceLine"]
      """  The Invoice Line Number of the APInvoiceMatch record  """  
      self.iVendorNum:int = obj["iVendorNum"]
      """  The Vendor Number of the APInvcRcptDtlMatch record  """  
      self.cPurPoint:str = obj["cPurPoint"]
      """  The Purchase Point of the APInvcRcptDtlMatch record  """  
      self.cPackSlip:str = obj["cPackSlip"]
      """  The Pack Slip of the APInvcRcptDtlMatch record  """  
      self.iPackLine:int = obj["iPackLine"]
      """  The Pack Slip Line of the APInvcRcptDtlMatch record  """  
      self.ds:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["ds"]
      pass

class MatchInvoiceReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APIRMtchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostMatches_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceMatchListTableset] = obj["ds"]
      pass

class PostMatches_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceMatchListTableset] = obj["ds"]
      self.cPostErrorLog:str = obj["parameters"]
      self.cErrorLogMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetSupplierXRefParts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierXRefTableset] = obj["ds"]
      pass

class SetSupplierXRefParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnMatchInvoiceReceipt_input:
   """ Required : 
   cInvoiceNum
   iInvoiceLine
   iVendorNum
   cPurPoint
   cPackSlip
   iPackLine
   ds
   """  
   def __init__(self, obj):
      self.cInvoiceNum:str = obj["cInvoiceNum"]
      """  The Invoice Number of the APInvcRcptDtlMatch record  """  
      self.iInvoiceLine:int = obj["iInvoiceLine"]
      """  The Invoice Line of the APInvcRcptDtlMatch record  """  
      self.iVendorNum:int = obj["iVendorNum"]
      """  The Vendor Number of the APInvcRcptDtlMatch record  """  
      self.cPurPoint:str = obj["cPurPoint"]
      """  The Purchase Point of the APInvcRcptDtlMatch record  """  
      self.cPackSlip:str = obj["cPackSlip"]
      """  The Pack Slip of the APInvcRcptDtlMatch record  """  
      self.iPackLine:int = obj["iPackLine"]
      """  The Pack Slip Line of the APInvcRcptDtlMatch record  """  
      self.ds:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["ds"]
      pass

class UnMatchInvoiceReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APIRMtchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceReceiptMatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

