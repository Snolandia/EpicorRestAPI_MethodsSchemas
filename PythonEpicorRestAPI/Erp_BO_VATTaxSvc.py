import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VATTaxSvc
# Description: Vat Tax front end
           Notes: if tttaxreport.posted = yes, then user should not be able to update
           any fields. Only allow 'post' menu option to be run for  tttaxreport.posted = no taxreport records.
           user should not be able to update posted, postedby, postdate fields.
           on post vat tax report screen, fill in with default report date from tttaxreport.reportdate, allow user override.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VATTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VATTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VATTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes",headers=creds) as resp:
           return await resp.json()

async def post_VATTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VATTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VATTaxes_Company_ReportID(Company, ReportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VATTax item
   Description: Calls GetByID to retrieve the VATTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VATTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VATTaxes_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VATTax for the service
   Description: Calls UpdateExt to update VATTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VATTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VATTaxes_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VATTax item
   Description: Call UpdateExt to delete VATTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VATTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxReport, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTaxReport=" + whereClauseTaxReport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDates
   Description: Check Dates, return any warnings
   OperationID: CheckDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreInitTaxRptDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreInitTaxRptDtl
   Description: Call this method to check if there are TaxRptDtl records that have been manually
updated or voided by the user.  This is to warn them that these records will not
be refreshed if they choose to continue with the InitializeTaxRptDtl method.
If the opMessage is not blank then show this to the user and let the user decide
whether to continue or not.  If the user answers yes then call InitializeTaxRptDtl.
   OperationID: PreInitTaxRptDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreInitTaxRptDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreInitTaxRptDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostReport
   Description: Call this method to check if there are TaxRptDtl records that have been manually
updated or voided by the user.  This is to warn them that these records will not
be refreshed if they choose to continue with the InitializeTaxRptDtl method.
If the opMessage is not blank then show this to the user and let the user decide
whether to continue or not.  If the user answers yes then call InitializeTaxRptDtl.
   OperationID: PrePostReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFiscalDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFiscalDates
   Description: Fills From/To dates according selected calendar, year and period if that is possible.
   OperationID: SetFiscalDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFiscalDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFiscalDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalCal
   Description: Validates Fiscal Calendar ID.
   OperationID: ValidateFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxReportRow] = obj["value"]
      pass

class Erp_Tablesets_TaxReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromTranDate:str = obj["FromTranDate"]
      """  From Transaction Date Parameter  """  
      self.ToTranDate:str = obj["ToTranDate"]
      """  To Transaction Date Parameter  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Sales tax report title  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that Posted this report.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date Parameter  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date Parameter  """  
      self.RptChecksum:str = obj["RptChecksum"]
      """  Report Checksum.  """  
      self.IncludeAP:bool = obj["IncludeAP"]
      """  Indicates Reporting to AP  """  
      self.IncludeAR:bool = obj["IncludeAR"]
      """  Indicates reporting to AR  """  
      self.SortBy:int = obj["SortBy"]
      """   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  """  
      self.TaxTypeList:str = obj["TaxTypeList"]
      """  Tax Type Filter  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability Filter  """  
      self.TaxJurisList:str = obj["TaxJurisList"]
      """  Tax Juridiction Filter  """  
      self.ReportCategoryList:str = obj["ReportCategoryList"]
      """  Report Category Filter  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer Filter  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier Filter  """  
      self.MXBalanceToCredit:int = obj["MXBalanceToCredit"]
      """  Balance To Credit (Mexico Localization field)  """  
      self.MXOnChargeToCredit:int = obj["MXOnChargeToCredit"]
      """  Charge To Credit (Mexico Localization field)  """  
      self.MXOnCountToCredit:int = obj["MXOnCountToCredit"]
      """  Count To Credit (Mexico Localization field)  """  
      self.MXCompesation:int = obj["MXCompesation"]
      """  Compensation (Mexico Localization field)  """  
      self.MXReimbursement:int = obj["MXReimbursement"]
      """  Reimbursement (Mexico Localization field)  """  
      self.MXWHSelected:int = obj["MXWHSelected"]
      """  WHSelected (Mexico Localization field)  """  
      self.MXTotalOnCharge:int = obj["MXTotalOnCharge"]
      """  Total On Charge (Mexico Localization field)  """  
      self.MXTotalOnCount:int = obj["MXTotalOnCount"]
      """  Total On Count (Mexico Localization field)  """  
      self.MXWithholdingVAT:int = obj["MXWithholdingVAT"]
      """  Withholding VAT (Mexico Localization field)  """  
      self.MXSurplusAmount:int = obj["MXSurplusAmount"]
      """  Surplus Amount (Mexico Localization field)  """  
      self.MXFiltersReady:bool = obj["MXFiltersReady"]
      """  Filters Ready (Mexico Localization field)  """  
      self.MXAllProportion:bool = obj["MXAllProportion"]
      """  All Proportion (Mexico Localization field)  """  
      self.MXReceiveMethod:str = obj["MXReceiveMethod"]
      """  Received Method (Mexico Localization field)  """  
      self.MXPropType:str = obj["MXPropType"]
      """  Proportion Type (Mexico Localization field)  """  
      self.MXChargeAmount:int = obj["MXChargeAmount"]
      """  Charge Amount (Mexico Localization field)  """  
      self.MXOnCountAmount:int = obj["MXOnCountAmount"]
      """  On Count Amount  (Mexico Localization field)  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar ID (Taiwan Localization field)  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  (Taiwan Localization field)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year (Taiwan Localization field)  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal Period  (Taiwan Localization field)  """  
      self.MXProportion:bool = obj["MXProportion"]
      """  Proportion (Mexico Localization field)  """  
      self.MXCurrMonth:int = obj["MXCurrMonth"]
      """  Current Month (Mexico Localization field)  """  
      self.RevReportCategoryList:str = obj["RevReportCategoryList"]
      """  Reverse Report Category Filter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Indicates if the Tax Box feature should be enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Fiscal calendar description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromTranDate:str = obj["FromTranDate"]
      """  From Transaction Date Parameter  """  
      self.ToTranDate:str = obj["ToTranDate"]
      """  To Transaction Date Parameter  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Sales tax report title  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that Posted this report.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date Parameter  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date Parameter  """  
      self.RptChecksum:str = obj["RptChecksum"]
      """  Report Checksum.  """  
      self.IncludeAP:bool = obj["IncludeAP"]
      """  Indicates Reporting to AP  """  
      self.IncludeAR:bool = obj["IncludeAR"]
      """  Indicates reporting to AR  """  
      self.SortBy:int = obj["SortBy"]
      """   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  """  
      self.TaxTypeList:str = obj["TaxTypeList"]
      """  Tax Type Filter  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability Filter  """  
      self.TaxJurisList:str = obj["TaxJurisList"]
      """  Tax Juridiction Filter  """  
      self.ReportCategoryList:str = obj["ReportCategoryList"]
      """  Report Category Filter  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer Filter  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier Filter  """  
      self.MXBalanceToCredit:int = obj["MXBalanceToCredit"]
      """  Balance To Credit (Mexico Localization field)  """  
      self.MXOnChargeToCredit:int = obj["MXOnChargeToCredit"]
      """  Charge To Credit (Mexico Localization field)  """  
      self.MXOnCountToCredit:int = obj["MXOnCountToCredit"]
      """  Count To Credit (Mexico Localization field)  """  
      self.MXCompesation:int = obj["MXCompesation"]
      """  Compensation (Mexico Localization field)  """  
      self.MXReimbursement:int = obj["MXReimbursement"]
      """  Reimbursement (Mexico Localization field)  """  
      self.MXWHSelected:int = obj["MXWHSelected"]
      """  WHSelected (Mexico Localization field)  """  
      self.MXTotalOnCharge:int = obj["MXTotalOnCharge"]
      """  Total On Charge (Mexico Localization field)  """  
      self.MXTotalOnCount:int = obj["MXTotalOnCount"]
      """  Total On Count (Mexico Localization field)  """  
      self.MXWithholdingVAT:int = obj["MXWithholdingVAT"]
      """  Withholding VAT (Mexico Localization field)  """  
      self.MXSurplusAmount:int = obj["MXSurplusAmount"]
      """  Surplus Amount (Mexico Localization field)  """  
      self.MXFiltersReady:bool = obj["MXFiltersReady"]
      """  Filters Ready (Mexico Localization field)  """  
      self.MXAllProportion:bool = obj["MXAllProportion"]
      """  All Proportion (Mexico Localization field)  """  
      self.MXReceiveMethod:str = obj["MXReceiveMethod"]
      """  Received Method (Mexico Localization field)  """  
      self.MXPropType:str = obj["MXPropType"]
      """  Proportion Type (Mexico Localization field)  """  
      self.MXChargeAmount:int = obj["MXChargeAmount"]
      """  Charge Amount (Mexico Localization field)  """  
      self.MXOnCountAmount:int = obj["MXOnCountAmount"]
      """  On Count Amount  (Mexico Localization field)  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar ID (Taiwan Localization field)  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  (Taiwan Localization field)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year (Taiwan Localization field)  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal Period  (Taiwan Localization field)  """  
      self.MXProportion:bool = obj["MXProportion"]
      """  Proportion (Mexico Localization field)  """  
      self.MXCurrMonth:int = obj["MXCurrMonth"]
      """  Current Month (Mexico Localization field)  """  
      self.RevReportCategoryList:str = obj["RevReportCategoryList"]
      """  Reverse Report Category Filter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DateBasis:str = obj["DateBasis"]
      """  DateBasis  """  
      self.BEAskPayment:bool = obj["BEAskPayment"]
      """  Demand Payment (CSF Belgium)  """  
      self.BERestitution:bool = obj["BERestitution"]
      """  Demand Restitution (CSF Belgium)  """  
      self.BEClientListing:bool = obj["BEClientListing"]
      """  Add Customer List (CSF Belgium)  """  
      self.BEDeclComment:str = obj["BEDeclComment"]
      """  Declaration Comment (CSF Belgium)  """  
      self.BEDeclLanguage:str = obj["BEDeclLanguage"]
      """  Declaration Language (CSF Belgium)  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Output File  """  
      self.BackDatedItems:int = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Indicates if the Tax Box feature should be enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Fiscal calendar description  """  
      self.SupplierIDList:str = obj["SupplierIDList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckDates_input:
   """ Required : 
   ds
   ipReportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      self.ipReportID:str = obj["ipReportID"]
      """  Report ID  """  
      pass

class CheckDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromTranDate:str = obj["FromTranDate"]
      """  From Transaction Date Parameter  """  
      self.ToTranDate:str = obj["ToTranDate"]
      """  To Transaction Date Parameter  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Sales tax report title  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that Posted this report.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date Parameter  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date Parameter  """  
      self.RptChecksum:str = obj["RptChecksum"]
      """  Report Checksum.  """  
      self.IncludeAP:bool = obj["IncludeAP"]
      """  Indicates Reporting to AP  """  
      self.IncludeAR:bool = obj["IncludeAR"]
      """  Indicates reporting to AR  """  
      self.SortBy:int = obj["SortBy"]
      """   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  """  
      self.TaxTypeList:str = obj["TaxTypeList"]
      """  Tax Type Filter  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability Filter  """  
      self.TaxJurisList:str = obj["TaxJurisList"]
      """  Tax Juridiction Filter  """  
      self.ReportCategoryList:str = obj["ReportCategoryList"]
      """  Report Category Filter  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer Filter  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier Filter  """  
      self.MXBalanceToCredit:int = obj["MXBalanceToCredit"]
      """  Balance To Credit (Mexico Localization field)  """  
      self.MXOnChargeToCredit:int = obj["MXOnChargeToCredit"]
      """  Charge To Credit (Mexico Localization field)  """  
      self.MXOnCountToCredit:int = obj["MXOnCountToCredit"]
      """  Count To Credit (Mexico Localization field)  """  
      self.MXCompesation:int = obj["MXCompesation"]
      """  Compensation (Mexico Localization field)  """  
      self.MXReimbursement:int = obj["MXReimbursement"]
      """  Reimbursement (Mexico Localization field)  """  
      self.MXWHSelected:int = obj["MXWHSelected"]
      """  WHSelected (Mexico Localization field)  """  
      self.MXTotalOnCharge:int = obj["MXTotalOnCharge"]
      """  Total On Charge (Mexico Localization field)  """  
      self.MXTotalOnCount:int = obj["MXTotalOnCount"]
      """  Total On Count (Mexico Localization field)  """  
      self.MXWithholdingVAT:int = obj["MXWithholdingVAT"]
      """  Withholding VAT (Mexico Localization field)  """  
      self.MXSurplusAmount:int = obj["MXSurplusAmount"]
      """  Surplus Amount (Mexico Localization field)  """  
      self.MXFiltersReady:bool = obj["MXFiltersReady"]
      """  Filters Ready (Mexico Localization field)  """  
      self.MXAllProportion:bool = obj["MXAllProportion"]
      """  All Proportion (Mexico Localization field)  """  
      self.MXReceiveMethod:str = obj["MXReceiveMethod"]
      """  Received Method (Mexico Localization field)  """  
      self.MXPropType:str = obj["MXPropType"]
      """  Proportion Type (Mexico Localization field)  """  
      self.MXChargeAmount:int = obj["MXChargeAmount"]
      """  Charge Amount (Mexico Localization field)  """  
      self.MXOnCountAmount:int = obj["MXOnCountAmount"]
      """  On Count Amount  (Mexico Localization field)  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar ID (Taiwan Localization field)  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  (Taiwan Localization field)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year (Taiwan Localization field)  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal Period  (Taiwan Localization field)  """  
      self.MXProportion:bool = obj["MXProportion"]
      """  Proportion (Mexico Localization field)  """  
      self.MXCurrMonth:int = obj["MXCurrMonth"]
      """  Current Month (Mexico Localization field)  """  
      self.RevReportCategoryList:str = obj["RevReportCategoryList"]
      """  Reverse Report Category Filter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Indicates if the Tax Box feature should be enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Fiscal calendar description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxReportListTableset:
   def __init__(self, obj):
      self.TaxReportList:list[Erp_Tablesets_TaxReportListRow] = obj["TaxReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromTranDate:str = obj["FromTranDate"]
      """  From Transaction Date Parameter  """  
      self.ToTranDate:str = obj["ToTranDate"]
      """  To Transaction Date Parameter  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Sales tax report title  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that Posted this report.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date Parameter  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date Parameter  """  
      self.RptChecksum:str = obj["RptChecksum"]
      """  Report Checksum.  """  
      self.IncludeAP:bool = obj["IncludeAP"]
      """  Indicates Reporting to AP  """  
      self.IncludeAR:bool = obj["IncludeAR"]
      """  Indicates reporting to AR  """  
      self.SortBy:int = obj["SortBy"]
      """   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  """  
      self.TaxTypeList:str = obj["TaxTypeList"]
      """  Tax Type Filter  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability Filter  """  
      self.TaxJurisList:str = obj["TaxJurisList"]
      """  Tax Juridiction Filter  """  
      self.ReportCategoryList:str = obj["ReportCategoryList"]
      """  Report Category Filter  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer Filter  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier Filter  """  
      self.MXBalanceToCredit:int = obj["MXBalanceToCredit"]
      """  Balance To Credit (Mexico Localization field)  """  
      self.MXOnChargeToCredit:int = obj["MXOnChargeToCredit"]
      """  Charge To Credit (Mexico Localization field)  """  
      self.MXOnCountToCredit:int = obj["MXOnCountToCredit"]
      """  Count To Credit (Mexico Localization field)  """  
      self.MXCompesation:int = obj["MXCompesation"]
      """  Compensation (Mexico Localization field)  """  
      self.MXReimbursement:int = obj["MXReimbursement"]
      """  Reimbursement (Mexico Localization field)  """  
      self.MXWHSelected:int = obj["MXWHSelected"]
      """  WHSelected (Mexico Localization field)  """  
      self.MXTotalOnCharge:int = obj["MXTotalOnCharge"]
      """  Total On Charge (Mexico Localization field)  """  
      self.MXTotalOnCount:int = obj["MXTotalOnCount"]
      """  Total On Count (Mexico Localization field)  """  
      self.MXWithholdingVAT:int = obj["MXWithholdingVAT"]
      """  Withholding VAT (Mexico Localization field)  """  
      self.MXSurplusAmount:int = obj["MXSurplusAmount"]
      """  Surplus Amount (Mexico Localization field)  """  
      self.MXFiltersReady:bool = obj["MXFiltersReady"]
      """  Filters Ready (Mexico Localization field)  """  
      self.MXAllProportion:bool = obj["MXAllProportion"]
      """  All Proportion (Mexico Localization field)  """  
      self.MXReceiveMethod:str = obj["MXReceiveMethod"]
      """  Received Method (Mexico Localization field)  """  
      self.MXPropType:str = obj["MXPropType"]
      """  Proportion Type (Mexico Localization field)  """  
      self.MXChargeAmount:int = obj["MXChargeAmount"]
      """  Charge Amount (Mexico Localization field)  """  
      self.MXOnCountAmount:int = obj["MXOnCountAmount"]
      """  On Count Amount  (Mexico Localization field)  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar ID (Taiwan Localization field)  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  (Taiwan Localization field)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year (Taiwan Localization field)  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal Period  (Taiwan Localization field)  """  
      self.MXProportion:bool = obj["MXProportion"]
      """  Proportion (Mexico Localization field)  """  
      self.MXCurrMonth:int = obj["MXCurrMonth"]
      """  Current Month (Mexico Localization field)  """  
      self.RevReportCategoryList:str = obj["RevReportCategoryList"]
      """  Reverse Report Category Filter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DateBasis:str = obj["DateBasis"]
      """  DateBasis  """  
      self.BEAskPayment:bool = obj["BEAskPayment"]
      """  Demand Payment (CSF Belgium)  """  
      self.BERestitution:bool = obj["BERestitution"]
      """  Demand Restitution (CSF Belgium)  """  
      self.BEClientListing:bool = obj["BEClientListing"]
      """  Add Customer List (CSF Belgium)  """  
      self.BEDeclComment:str = obj["BEDeclComment"]
      """  Declaration Comment (CSF Belgium)  """  
      self.BEDeclLanguage:str = obj["BEDeclLanguage"]
      """  Declaration Language (CSF Belgium)  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Output File  """  
      self.BackDatedItems:int = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Indicates if the Tax Box feature should be enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Fiscal calendar description  """  
      self.SupplierIDList:str = obj["SupplierIDList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtVATTaxTableset:
   def __init__(self, obj):
      self.TaxReport:list[Erp_Tablesets_TaxReportRow] = obj["TaxReport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VATTaxTableset:
   def __init__(self, obj):
      self.TaxReport:list[Erp_Tablesets_TaxReportRow] = obj["TaxReport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VATTaxTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VATTaxTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VATTaxTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

class GetNewTaxReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxReport
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxReport:str = obj["whereClauseTaxReport"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VATTaxTableset] = obj["returnObj"]
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

class PreInitTaxRptDtl_input:
   """ Required : 
   ipReportID
   """  
   def __init__(self, obj):
      self.ipReportID:str = obj["ipReportID"]
      """  The VAT Tax Report ID.  """  
      pass

class PreInitTaxRptDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrePostReport_input:
   """ Required : 
   inputReportID
   inputUpdTaxRptDtl
   """  
   def __init__(self, obj):
      self.inputReportID:str = obj["inputReportID"]
      """  report id of report to be posted.  """  
      self.inputUpdTaxRptDtl:bool = obj["inputUpdTaxRptDtl"]
      """  Indicates if the TaxRptDtl will be updated or not.  """  
      pass

class PrePostReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetFiscalDates_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

class SetFiscalDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVATTaxTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVATTaxTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFiscalCal_input:
   """ Required : 
   ds
   fiscalCalID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      self.fiscalCalID:str = obj["fiscalCalID"]
      """  The fiscal calendar ID  """  
      pass

class ValidateFiscalCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VATTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

