import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GetAmortizationSvc
# Description: Get Deferred Revenue Amortization Schedules object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetAmortizations(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GetAmortizations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GetAmortizations
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations",headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GetAmortizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company, InvoiceNum, InvoiceLine, AmortSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GetAmortization item
   Description: Calls GetByID to retrieve the GetAmortization item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GetAmortization
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company, InvoiceNum, InvoiceLine, AmortSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GetAmortization for the service
   Description: Calls UpdateExt to update GetAmortization. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GetAmortization
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company, InvoiceNum, InvoiceLine, AmortSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GetAmortization item
   Description: Call UpdateExt to delete GetAmortization item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GetAmortization
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRaschListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseInvcDtlRASch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseInvcDtlRASch=" + whereClauseInvcDtlRASch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(invoiceNum, invoiceLine, amortSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "amortSeq=" + amortSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildAmortizationsLists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAmortizationsLists
   Description: This method returns four possible lists of selected Deferred Revenue Amortization
Schedules (ttInvcDtlRASch).  This should be called to return a list containing the
key fields of selected InvcDtlRASch records. Since each record has three key fields
the list could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into four lists if needed.
   OperationID: BuildAmortizationsLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAmortizationsLists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAmortizationsLists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizations
   Description: This method returns the ttInvcDtlRASch dataset of Deferred Revenue Amortization Schedule with
some calculated columns added.
   OperationID: GetAmortizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizationsWithTotal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizationsWithTotal
   Description: This method returns the ttInvcDtlRASch dataset of Deferred Revenue Amortization Schedule with
some calculated columns added.
   OperationID: GetAmortizationsWithTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationsWithTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationsWithTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizationRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizationRows
   Description: Returns Amortizations tableset for search
   OperationID: GetAmortizationRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizationTotal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizationTotal
   Description: This method calculates the amortization total based on records in the GetAmortization tableset
   OperationID: GetAmortizationTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base Currency
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcDtlRASch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcDtlRASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtlRASch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtlRASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtlRASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRASchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlRASchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRaschListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlRaschListRow] = obj["value"]
      pass

class Erp_Tablesets_InvcDtlRASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AmortDate:str = obj["AmortDate"]
      """  This is the date when the percentage of revenue will be recognized.  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  This is the percentage of total revenue to be recognized.  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  Amortization Amount of the invoice.  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  The amount to be recognized in the first reporting currency.  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  The amortization amount in the reporting currency.  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  The amortization in reporting currency.  """  
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      """  The amortization amount in document currency.  """  
      self.Hold:bool = obj["Hold"]
      """  Indicates if this amortization period is on hold.  """  
      self.HoldReasonCode:str = obj["HoldReasonCode"]
      """  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  """  
      self.HoldText:str = obj["HoldText"]
      """  Descriptive text further explaining why an amortization period is on hold.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if the revenue has been recognized for this line.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  The date when the revenue was recognized.  """  
      self.ContractNum:int = obj["ContractNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrgAmortSeq:int = obj["OrgAmortSeq"]
      """  Internal identifier used to Keep the records unique. Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.OrgInvcLine:int = obj["OrgInvcLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustID:str = obj["CustID"]
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      self.DocDspAmortAmt:int = obj["DocDspAmortAmt"]
      self.DocDspRevenueAmt:int = obj["DocDspRevenueAmt"]
      self.DocRevenueAmt:int = obj["DocRevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  """  
      self.DspAmortAmt:int = obj["DspAmortAmt"]
      self.DspRevenueAmt:int = obj["DspRevenueAmt"]
      self.GroupID:str = obj["GroupID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date is coming from the InvcHead.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      self.RevenueAmt:int = obj["RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount).  """  
      self.Rpt1DspAmortAmt:int = obj["Rpt1DspAmortAmt"]
      self.Rpt1DspRevenueAmt:int = obj["Rpt1DspRevenueAmt"]
      self.Rpt1RevenueAmt:int = obj["Rpt1RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt2DspAmortAmt:int = obj["Rpt2DspAmortAmt"]
      self.Rpt2DspRevenueAmt:int = obj["Rpt2DspRevenueAmt"]
      self.Rpt2RevenueAmt:int = obj["Rpt2RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt3DspAmortAmt:int = obj["Rpt3DspAmortAmt"]
      self.Rpt3DspRevenueAmt:int = obj["Rpt3DspRevenueAmt"]
      self.Rpt3RevenueAmt:int = obj["Rpt3RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Selected:bool = obj["Selected"]
      """  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  """  
      self.SeqDuration:str = obj["SeqDuration"]
      """  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  """  
      self.TotalAmortAmt:int = obj["TotalAmortAmt"]
      """  Total Amortization Amount of all the periods displayed on the grid in base currency.  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an Schedule line is already in review journal or in posting process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcDtlRaschListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AmortDate:str = obj["AmortDate"]
      """  This is the date when the percentage of revenue will be recognized.  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  This is the percentage of total revenue to be recognized.  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  Amortization Amount of the invoice.  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  The amount to be recognized in the first reporting currency.  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  The amortization amount in the reporting currency.  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  The amortization in reporting currency.  """  
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      """  The amortization amount in document currency.  """  
      self.Hold:bool = obj["Hold"]
      """  Indicates if this amortization period is on hold.  """  
      self.HoldReasonCode:str = obj["HoldReasonCode"]
      """  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  """  
      self.HoldText:str = obj["HoldText"]
      """  Descriptive text further explaining why an amortization period is on hold.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if the revenue has been recognized for this line.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  The date when the revenue was recognized.  """  
      self.ContractNum:int = obj["ContractNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      self.ReadyToPost:bool = obj["ReadyToPost"]
      self.Selected:bool = obj["Selected"]
      """  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  """  
      self.CustID:str = obj["CustID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date is coming from the InvcHead.  """  
      self.RevenueAmt:int = obj["RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount).  """  
      self.DocRevenueAmt:int = obj["DocRevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  """  
      self.Rpt1RevenueAmt:int = obj["Rpt1RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt2RevenueAmt:int = obj["Rpt2RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt3RevenueAmt:int = obj["Rpt3RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.TotalAmortAmt:int = obj["TotalAmortAmt"]
      """  Total Amortization Amount of all the periods displayed on the grid in base currency.  """  
      self.SeqDuration:str = obj["SeqDuration"]
      """  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildAmortizationsLists_input:
   """ Required : 
   opGuid
   ds
   """  
   def __init__(self, obj):
      self.opGuid:str = obj["opGuid"]
      """  Unique Identifier  """  
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class BuildAmortizationsLists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opReasonMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   invoiceNum
   invoiceLine
   amortSeq
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.amortSeq:int = obj["amortSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GetAmortizationTableset:
   def __init__(self, obj):
      self.InvcDtlRASch:list[Erp_Tablesets_InvcDtlRASchRow] = obj["InvcDtlRASch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcDtlRASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AmortDate:str = obj["AmortDate"]
      """  This is the date when the percentage of revenue will be recognized.  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  This is the percentage of total revenue to be recognized.  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  Amortization Amount of the invoice.  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  The amount to be recognized in the first reporting currency.  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  The amortization amount in the reporting currency.  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  The amortization in reporting currency.  """  
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      """  The amortization amount in document currency.  """  
      self.Hold:bool = obj["Hold"]
      """  Indicates if this amortization period is on hold.  """  
      self.HoldReasonCode:str = obj["HoldReasonCode"]
      """  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  """  
      self.HoldText:str = obj["HoldText"]
      """  Descriptive text further explaining why an amortization period is on hold.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if the revenue has been recognized for this line.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  The date when the revenue was recognized.  """  
      self.ContractNum:int = obj["ContractNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrgAmortSeq:int = obj["OrgAmortSeq"]
      """  Internal identifier used to Keep the records unique. Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.OrgInvcLine:int = obj["OrgInvcLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustID:str = obj["CustID"]
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      self.DocDspAmortAmt:int = obj["DocDspAmortAmt"]
      self.DocDspRevenueAmt:int = obj["DocDspRevenueAmt"]
      self.DocRevenueAmt:int = obj["DocRevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  """  
      self.DspAmortAmt:int = obj["DspAmortAmt"]
      self.DspRevenueAmt:int = obj["DspRevenueAmt"]
      self.GroupID:str = obj["GroupID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date is coming from the InvcHead.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      self.RevenueAmt:int = obj["RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount).  """  
      self.Rpt1DspAmortAmt:int = obj["Rpt1DspAmortAmt"]
      self.Rpt1DspRevenueAmt:int = obj["Rpt1DspRevenueAmt"]
      self.Rpt1RevenueAmt:int = obj["Rpt1RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt2DspAmortAmt:int = obj["Rpt2DspAmortAmt"]
      self.Rpt2DspRevenueAmt:int = obj["Rpt2DspRevenueAmt"]
      self.Rpt2RevenueAmt:int = obj["Rpt2RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt3DspAmortAmt:int = obj["Rpt3DspAmortAmt"]
      self.Rpt3DspRevenueAmt:int = obj["Rpt3DspRevenueAmt"]
      self.Rpt3RevenueAmt:int = obj["Rpt3RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Selected:bool = obj["Selected"]
      """  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  """  
      self.SeqDuration:str = obj["SeqDuration"]
      """  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  """  
      self.TotalAmortAmt:int = obj["TotalAmortAmt"]
      """  Total Amortization Amount of all the periods displayed on the grid in base currency.  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an Schedule line is already in review journal or in posting process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcDtlRaschListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AmortDate:str = obj["AmortDate"]
      """  This is the date when the percentage of revenue will be recognized.  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  This is the percentage of total revenue to be recognized.  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  Amortization Amount of the invoice.  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  The amount to be recognized in the first reporting currency.  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  The amortization amount in the reporting currency.  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  The amortization in reporting currency.  """  
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      """  The amortization amount in document currency.  """  
      self.Hold:bool = obj["Hold"]
      """  Indicates if this amortization period is on hold.  """  
      self.HoldReasonCode:str = obj["HoldReasonCode"]
      """  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  """  
      self.HoldText:str = obj["HoldText"]
      """  Descriptive text further explaining why an amortization period is on hold.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if the revenue has been recognized for this line.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  The date when the revenue was recognized.  """  
      self.ContractNum:int = obj["ContractNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      self.ReadyToPost:bool = obj["ReadyToPost"]
      self.Selected:bool = obj["Selected"]
      """  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  """  
      self.CustID:str = obj["CustID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date is coming from the InvcHead.  """  
      self.RevenueAmt:int = obj["RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount).  """  
      self.DocRevenueAmt:int = obj["DocRevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  """  
      self.Rpt1RevenueAmt:int = obj["Rpt1RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt2RevenueAmt:int = obj["Rpt2RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.Rpt3RevenueAmt:int = obj["Rpt3RevenueAmt"]
      """  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  """  
      self.TotalAmortAmt:int = obj["TotalAmortAmt"]
      """  Total Amortization Amount of all the periods displayed on the grid in base currency.  """  
      self.SeqDuration:str = obj["SeqDuration"]
      """  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcDtlRaschListTableset:
   def __init__(self, obj):
      self.InvcDtlRaschList:list[Erp_Tablesets_InvcDtlRaschListRow] = obj["InvcDtlRaschList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGetAmortizationTableset:
   def __init__(self, obj):
      self.InvcDtlRASch:list[Erp_Tablesets_InvcDtlRASchRow] = obj["InvcDtlRASch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAmortizationRows_input:
   """ Required : 
   ipCustList
   ipInvList
   ipContList
   ipApplyDate
   ipShowStatus
   ds
   """  
   def __init__(self, obj):
      self.ipCustList:str = obj["ipCustList"]
      self.ipInvList:str = obj["ipInvList"]
      self.ipContList:str = obj["ipContList"]
      self.ipApplyDate:str = obj["ipApplyDate"]
      self.ipShowStatus:str = obj["ipShowStatus"]
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class GetAmortizationRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GetAmortizationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.totalAmortization:int = obj["parameters"]
      self.baseCurrencyCode:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAmortizationTotal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class GetAmortizationTotal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.amortizationTotal:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAmortizationsWithTotal_input:
   """ Required : 
   ipCustList
   ipInvList
   ipContList
   ipApplyDate
   ipShowStatus
   ds
   """  
   def __init__(self, obj):
      self.ipCustList:str = obj["ipCustList"]
      """  The Customer Number list to filter the records with  """  
      self.ipInvList:str = obj["ipInvList"]
      """  The Invoice Number list to filter the records with  """  
      self.ipContList:str = obj["ipContList"]
      """  The Service Contract Number list to filter the records with  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  The Apply Date filter  """  
      self.ipShowStatus:str = obj["ipShowStatus"]
      """  If value is 'H', show records marked as On Hold; if 'U', show records Not On Hold; if 'B', show all.  """  
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class GetAmortizationsWithTotal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalAmortization:int = obj["parameters"]
      self.baseCurrencyCode:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAmortizations_input:
   """ Required : 
   ipCustList
   ipInvList
   ipContList
   ipApplyDate
   ipShowStatus
   ds
   """  
   def __init__(self, obj):
      self.ipCustList:str = obj["ipCustList"]
      """  The Customer Number list to filter the records with  """  
      self.ipInvList:str = obj["ipInvList"]
      """  The Invoice Number list to filter the records with  """  
      self.ipContList:str = obj["ipContList"]
      """  The Service Contract Number list to filter the records with  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  The Apply Date filter  """  
      self.ipShowStatus:str = obj["ipShowStatus"]
      """  If value is 'H', show records marked as On Hold; if 'U', show records Not On Hold; if 'B', show all.  """  
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class GetAmortizations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   invoiceNum
   invoiceLine
   amortSeq
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.amortSeq:int = obj["amortSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GetAmortizationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GetAmortizationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GetAmortizationTableset] = obj["returnObj"]
      pass

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
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
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcDtlRaschListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcDtlRASch_input:
   """ Required : 
   ds
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class GetNewInvcDtlRASch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseInvcDtlRASch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcDtlRASch:str = obj["whereClauseInvcDtlRASch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GetAmortizationTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGetAmortizationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGetAmortizationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetAmortizationTableset] = obj["ds"]
      pass

      """  output parameters  """  

