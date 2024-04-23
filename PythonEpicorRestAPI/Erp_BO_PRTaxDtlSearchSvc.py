import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PRTaxDtlSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRTaxDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_PRTaxDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxDtlSearch item
   Description: Calls GetByID to retrieve the PRTaxDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRTaxDtlSearch for the service
   Description: Calls UpdateExt to update PRTaxDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRTaxDtlSearch item
   Description: Call UpdateExt to delete PRTaxDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRTaxDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePRTaxDtl=" + whereClausePRTaxDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxTblID, fileStatus, taxYear, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "taxTblID=" + taxTblID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fileStatus=" + fileStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taxYear=" + taxYear

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Returns a list of rows that satisfy the where clause and removes duplicate rows.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxDtlRow] = obj["value"]
      pass

class Erp_Tablesets_PRTaxDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   taxTblID
   fileStatus
   taxYear
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      self.fileStatus:str = obj["fileStatus"]
      self.taxYear:int = obj["taxYear"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PRTaxDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxDtlListTableset:
   def __init__(self, obj):
      self.PRTaxDtlList:list[Erp_Tablesets_PRTaxDtlListRow] = obj["PRTaxDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxDtlSearchTableset:
   def __init__(self, obj):
      self.PRTaxDtl:list[Erp_Tablesets_PRTaxDtlRow] = obj["PRTaxDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPRTaxDtlSearchTableset:
   def __init__(self, obj):
      self.PRTaxDtl:list[Erp_Tablesets_PRTaxDtlRow] = obj["PRTaxDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   taxTblID
   fileStatus
   taxYear
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      self.fileStatus:str = obj["fileStatus"]
      self.taxYear:int = obj["taxYear"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
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

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRTaxDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_PRTaxDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPRTaxDtl_input:
   """ Required : 
   ds
   taxTblID
   fileStatus
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["ds"]
      self.taxTblID:str = obj["taxTblID"]
      self.fileStatus:str = obj["fileStatus"]
      pass

class GetNewPRTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRTaxDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRTaxDtl:str = obj["whereClausePRTaxDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPRTaxDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPRTaxDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRTaxDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

