import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PREmployeeSvc
# Description: Payroll Employee Maintenance consists of:
1) Payroll Employee Deduction master.
This file establishes which deduction, the amount of deduction
and when it is to be taken for a specific employee.
2)Payroll Employee master.
This file is an extension of the data stored in the EmpBasic file.
All of the data fields stored in EmpBasic also exist in PREmpMas.
They are kept in sync via write triggers on both the EmpBasic/PREmpMas.
The existence of this record indicates that this employee is set up in the payroll system.
3) Payroll employee master rate file.
4) Payroll Employee Tax file.
Establishes the different taxes that are relevant for an employee.
Subset to the PREmpMas file.
Notes: 2 of sort options are based on the PREmpMas.Terminated Flag
The 3rd sort option browses on the EmpBasic table where PRSetupReq is true
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PREmployees items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmployees
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees",headers=creds) as resp:
           return await resp.json()

async def post_PREmployees(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID(Company, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmployee item
   Description: Calls GetByID to retrieve the PREmployee item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PREmployees_Company_EmpID(Company, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PREmployee for the service
   Description: Calls UpdateExt to update PREmployee. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PREmployees_Company_EmpID(Company, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PREmployee item
   Description: Call UpdateExt to delete PREmployee item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpDeds(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PREmpDeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpDeds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpDeds",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company, EmpID, EmpLink, DeductionID, DeductionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpDed item
   Description: Calls GetByID to retrieve the PREmpDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpDed1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpRts(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PREmpRts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpRts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpRts",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpRts_Company_EmpLink_RateDate(Company, EmpID, EmpLink, RateDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpRt item
   Description: Calls GetByID to retrieve the PREmpRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpRt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param RateDate: Desc: RateDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpTaxes(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PREmpTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpTaxes",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpTaxes_Company_EmpLink_TaxTblID(Company, EmpID, EmpLink, TaxTblID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpTax item
   Description: Calls GetByID to retrieve the PREmpTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_EntityGLCs(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, EmpID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpMasAttches(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PREmpMasAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpMasAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpMasAttches",headers=creds) as resp:
           return await resp.json()

async def get_PREmployees_Company_EmpID_PREmpMasAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpMasAttch item
   Description: Calls GetByID to retrieve the PREmpMasAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpMasAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmpDeds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PREmpDeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpDeds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds",headers=creds) as resp:
           return await resp.json()

async def post_PREmpDeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpDeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company, EmpLink, DeductionID, DeductionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpDed item
   Description: Calls GetByID to retrieve the PREmpDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company, EmpLink, DeductionID, DeductionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PREmpDed for the service
   Description: Calls UpdateExt to update PREmpDed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company, EmpLink, DeductionID, DeductionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PREmpDed item
   Description: Call UpdateExt to delete PREmpDed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmpRts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PREmpRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpRts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts",headers=creds) as resp:
           return await resp.json()

async def post_PREmpRts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PREmpRts_Company_EmpLink_RateDate(Company, EmpLink, RateDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpRt item
   Description: Calls GetByID to retrieve the PREmpRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param RateDate: Desc: RateDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PREmpRts_Company_EmpLink_RateDate(Company, EmpLink, RateDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PREmpRt for the service
   Description: Calls UpdateExt to update PREmpRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param RateDate: Desc: RateDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PREmpRts_Company_EmpLink_RateDate(Company, EmpLink, RateDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PREmpRt item
   Description: Call UpdateExt to delete PREmpRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param RateDate: Desc: RateDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmpTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PREmpTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PREmpTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PREmpTaxes_Company_EmpLink_TaxTblID(Company, EmpLink, TaxTblID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpTax item
   Description: Calls GetByID to retrieve the PREmpTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PREmpTaxes_Company_EmpLink_TaxTblID(Company, EmpLink, TaxTblID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PREmpTax for the service
   Description: Calls UpdateExt to update PREmpTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PREmpTaxes_Company_EmpLink_TaxTblID(Company, EmpLink, TaxTblID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PREmpTax item
   Description: Call UpdateExt to delete PREmpTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpLink: Desc: EmpLink   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PREmpMasAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PREmpMasAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpMasAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches",headers=creds) as resp:
           return await resp.json()

async def post_PREmpMasAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpMasAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PREmpMasAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PREmpMasAttch item
   Description: Calls GetByID to retrieve the PREmpMasAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpMasAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PREmpMasAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PREmpMasAttch for the service
   Description: Calls UpdateExt to update PREmpMasAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpMasAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PREmpMasAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PREmpMasAttch item
   Description: Call UpdateExt to delete PREmpMasAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpMasAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Partners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners",headers=creds) as resp:
           return await resp.json()

async def post_Partners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePREmpMas, whereClausePREmpMasAttch, whereClausePREmpDed, whereClausePREmpRt, whereClausePREmpTax, whereClauseEntityGLC, whereClausePartner, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClausePREmpMas=" + whereClausePREmpMas
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePREmpMasAttch=" + whereClausePREmpMasAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePREmpDed=" + whereClausePREmpDed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePREmpRt=" + whereClausePREmpRt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePREmpTax=" + whereClausePREmpTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartner=" + whereClausePartner
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, epicorHeaders = None):
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
   params += "empID=" + empID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddEmployeeResultsLinkCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddEmployeeResultsLinkCompany
   Description: This method will add employee results link to all employees in the company
   OperationID: AddEmployeeResultsLinkCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddEmployeeResultsLinkCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddEmployeeResultsLinkCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildClassList(epicorHeaders = None):
   """  
   Summary: Invoke method BuildClassList
   Description: This method returns a list of valid Classes to select from for the user's security
   OperationID: BuildClassList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildClassList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_BuildFilingList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildFilingList
   Description: This method returns a list of filing status' based on the TaxTable ID selected
   OperationID: BuildFilingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildFilingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildFilingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildTaxTblList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildTaxTblList
   Description: This method generates a list of TaxTbls available to choose from when Adding/Updating
a PREmpTax record
   OperationID: BuildTaxTblList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildTaxTblList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTaxTblList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcSalaryRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcSalaryRate
   Description: This method updates the salary or rate field on PREmpRt when the other field is updated
It is to be run after either Salary or PayRate is updated.
   OperationID: CalcSalaryRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSalaryRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSalaryRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFileStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFileStatus
   Description: This method should run when the JobMtl.Plant field changes.
This method determines the default JobMtl.WarehouseCode associated with the new JobMtl.Plant.
   OperationID: ChangeFileStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFileStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFileStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPayRateEffectiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPayRateEffectiveDate
   Description: This method checks if the first pay rate effective date is different than the hire date.  Returns an
informational message if it is.
   OperationID: CheckPayRateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPayRateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayRateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPersonContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPersonContact
   Description: Checks if the Person Contact ID is already assigned to another Payroll Employee
   OperationID: CheckPersonContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPersonContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPersonContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJCDeptExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJCDeptExists
   Description: This method checks if the JCDept record exists.
   OperationID: CheckJCDeptExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJCDeptExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJCDeptExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLaborExpCodeExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckLaborExpCodeExists
   Description: This method checks if the LabExpCd record exists.
   OperationID: CheckLaborExpCodeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLaborExpCodeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLaborExpCodeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLeavePREmpMas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckLeavePREmpMas
   Description: This method checks if a PREmpRt record exists for the current employee record
if no record exists then the user cannot leave the record until they create a rate
record or delete the employee record.
   OperationID: CheckLeavePREmpMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLeavePREmpMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLeavePREmpMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPRClassExisst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPRClassExisst
   Description: This method checks if the PRClass record exists.
   OperationID: CheckPRClassExisst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRClassExisst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRClassExisst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPRWorkCompCodeExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPRWorkCompCodeExists
   Description: This method checks if the PRWrkCmp record exists.
   OperationID: CheckPRWorkCompCodeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRWorkCompCodeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRWorkCompCodeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeductDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeductDefaults
   Description: This method sets the deduction defaults once the DeductionID is selected
   OperationID: GetDeductDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeductDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeductDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmpIDInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpIDInfo
   Description: This method will default the name and address information from EmpBasic if
the EmpId entered exists in EmpBasic
   OperationID: GetEmpIDInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpIDInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpIDInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmpLinkValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpLinkValue
   Description: Gets Employee Link
   OperationID: GetEmpLinkValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpLinkValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpLinkValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShopEmployee(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShopEmployee
   Description: This method creates a new PREmpMas record based on information from the EmpBasic record. It
takes EmpID as a parameter.
The standard GetNewPREmpMas method will be used when adding a new Payroll Employee from scratch.
   OperationID: GetNewShopEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShopEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShopEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOverrideList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOverrideList
   Description: This method is identical to the GetList method except that it overrides the
PREmpMas find trigger and will return all Employees, not just the ones the user has
clearance for.  This is mainly for the SupervisorID lookups for Shop and Payroll employee
maintenance
   OperationID: GetOverrideList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOverrideList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOverrideList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShopEmployeeInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShopEmployeeInfo
   Description: This method is called for a new employee. If the employee exists in the
EmpBasic table the data will be defaulted in the PREmployee record.
   OperationID: GetShopEmployeeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShopEmployeeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShopEmployeeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveEmployeeResultsLinkCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveEmployeeResultsLinkCompany
   Description: This method will add employee results link to all employees in the company
   OperationID: RemoveEmployeeResultsLinkCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveEmployeeResultsLinkCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveEmployeeResultsLinkCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRequiredFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRequiredFields
   Description: Purpose: This method will validate that all required fields have valid data before activate an Employee
<param name="ds">PREmploye Entry data set</param>
   OperationID: ValidateRequiredFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRequiredFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRequiredFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePayRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePayRate
   Description: Purpose: This method will validate that a rate has not a duplicated rateDate for an employee
<param name="empLink">empLink field in PREmpRt</param><param name="rateDate">rateDate field in PREmpRt</param>
   OperationID: ValidatePayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifySearchIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPREmpMas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPREmpMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPREmpMasAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPREmpMasAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpMasAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpMasAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpMasAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPREmpDed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPREmpDed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPREmpRt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPREmpRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPREmpTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPREmpTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpDedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpMasAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpMasListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpMasRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpRtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PREmpTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartnerRow] = obj["value"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpDedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  encoded value which identifies the employee.  """  
      self.DeductionID:str = obj["DeductionID"]
      """  The ID of the related deduction master  """  
      self.DeductionNum:int = obj["DeductionNum"]
      """  DeductionNum uniquely identifies a PREmpDed record for an employee, for a specific DeductionID.  This enables an employee to have the same Deduction established more than once without having to set up a new deduction master.  For example, you may have a deduction for loan repayments and the employee may have multiple loans each with there own declining balances established.  This integer is assigned by the system automatically by finding the last related records number and adding one to it.  """  
      self.Period1:bool = obj["Period1"]
      """  Indicates that this deduction is taken during deduction period 1. Deduction periods (of which there are five) provide a method of controlling when the deduction is to be taken.  When payroll is run you are asked to enter a deduction period.  Only deductions that have that period marked will be taken. An exception to this rule would be if the CarryOverAmt <> 0 (see CarryOverAmt).  """  
      self.Period2:bool = obj["Period2"]
      """  Indicates that this deduction is taken during deduction period 2.  (Also see Period1).  """  
      self.Period3:bool = obj["Period3"]
      """  Indicates if this deduction is taken during deduction period 3.  (Also see Period1).  """  
      self.Period4:bool = obj["Period4"]
      """  Indicates if this deduction is taken during deduction period 4.  (Also see Period1).  """  
      self.Period5:bool = obj["Period5"]
      """  Indicates if this deduction is taken during deduction period 5.  (Also see Period1).  """  
      self.Rate:int = obj["Rate"]
      """  Deduction Rate.  This can represent either a fixed amount or a percent of gross wages (see RateQualifier).  """  
      self.RateQualifier:str = obj["RateQualifier"]
      """   The value of this field qualifies the value stored in the Rate field as either a fixed amount, percent of gross or percent of net pay. Defaulted from PRDeduct.RateQualifier.
Amt = Amount,  %Grs = Percent of gross, %Net = Percent of Net.
Note:  %Net is not allowed if the deduction is exempt from any taxes (records in PRDedXTx).  if %Net then this deduction is calculated after all other deductions and taxes, regardless of the deduction being tax exempt.  A deduction could be %Net and marked as tax exempt if the deduction was made tax exempt after it had already been marked as %Net.  """  
      self.DeclineOrigAmt:int = obj["DeclineOrigAmt"]
      """  This is the original amount of the declining deduction.  It is used primarily as a reference.  """  
      self.DeclineRemAmt:int = obj["DeclineRemAmt"]
      """  This is the remaining amount of the declining deduction.  """  
      self.CheckLimit:int = obj["CheckLimit"]
      """  This value sets a maximum check limit on the amount of this deduction.  """  
      self.MonthLimit:int = obj["MonthLimit"]
      """  This value sets a maximum monthly limit on the amount of this deduction.  The month is determined by using the check date.  """  
      self.YearlyLimit:int = obj["YearlyLimit"]
      """  This value sets a maximum yearly limit on the amount of this deduction.  The year is determined by using the check date.  """  
      self.CarryOverAmt:int = obj["CarryOverAmt"]
      """  Amount carried over from previous pay period.  The system will attempt to deduct this amount in the very next pay period regardless of the deduction cycle.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. Inactive = Yes prevents the deduction from being taken.  """  
      self.Reference:str = obj["Reference"]
      """  Employee specific information that can be used to further describe the reason for the deduction. For example; you may have a generic deduction called "Purchases", using the reference you could identify what the employee's purchase was. This field is printed on the check stub.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific deduction.  """  
      self.BankRoutingNum:str = obj["BankRoutingNum"]
      """  Employee's Bank Routing Number  """  
      self.BankAcctNum:str = obj["BankAcctNum"]
      """  Employee's Bank Account Number  """  
      self.BankAcctName:str = obj["BankAcctName"]
      """  The name the employee's bank account is under.  It doesn't have to match the employee's name.  """  
      self.BankAcctType:str = obj["BankAcctType"]
      """  The employee's bank account type:  C - Checking, S - Savings, etc.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      self.ElecDeposit:bool = obj["ElecDeposit"]
      self.CarryOver:bool = obj["CarryOver"]
      self.DeclineBalance:bool = obj["DeclineBalance"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.DeductionDescription:str = obj["DeductionDescription"]
      self.DeductionHCMLinked:bool = obj["DeductionHCMLinked"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.SocSecNum:str = obj["SocSecNum"]
      """  Encrypted Social security number.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.ClassID:str = obj["ClassID"]
      """   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  """  
      self.HireDate:str = obj["HireDate"]
      """  Date that employee was hired.  """  
      self.Terminated:bool = obj["Terminated"]
      """  Indicates if employee has been terminated.  """  
      self.TerminatedDate:str = obj["TerminatedDate"]
      """  Date that employee was terminated from employment.  """  
      self.PayType:str = obj["PayType"]
      """  H = Hourly,  S = Salaried.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  """  
      self.ShopEmployee:bool = obj["ShopEmployee"]
      """  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the payroll employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspSocSecNum:str = obj["DspSocSecNum"]
      """  Unencrypted Social Security Number for input and display purposes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value for employee which can be used to link the PREmpMas with it's sub related files.  This field is normally blank, which means file joins are impossible. This value can be set/reset only by the payroll manager via an option in system maintenance.  """  
      self.SocSecNum:str = obj["SocSecNum"]
      """  Encrypted Social security number.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.ClassID:str = obj["ClassID"]
      """   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.HireDate:str = obj["HireDate"]
      """  Date that employee was hired.  """  
      self.Terminated:bool = obj["Terminated"]
      """  Indicates if employee has been terminated.  """  
      self.TerminatedDate:str = obj["TerminatedDate"]
      """  Date that employee was terminated from employment.  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Employees birthday  """  
      self.PayType:str = obj["PayType"]
      """  H = Hourly,  S = Salaried.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  """  
      self.Pension:bool = obj["Pension"]
      """  Indicates if this employee is part of a pension plan.  This is used to print on the W2 form  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Indicates if this employee is part of a deferred compensation plan.  This is used to print on the W2 form  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The workman's compensation master that this employee is related to.  """  
      self.VacAccrualRate:int = obj["VacAccrualRate"]
      """  The number of hours of vacation time that is earned per pay period.  """  
      self.VacRemaining:int = obj["VacRemaining"]
      """  Vacation hours remaining. This field can be updated through master maintenance.  It is increased by the VacAccuralRate value for each period the employee is paid. It is reduced when vacation hours are entered in check entry.  """  
      self.VacHrsMax:int = obj["VacHrsMax"]
      """  Maximum number of vacation hours that can be accrued.  """  
      self.SickAccrualRate:int = obj["SickAccrualRate"]
      """  The number of hours of sick time that is earned per pay period.  """  
      self.SickRemaining:int = obj["SickRemaining"]
      """  Total Sick hours remaining.  This field can be directly maintained via employee master maintenance.  It gets increased by the SickAccrualRate value for each period an employee gets paid in.  It is decreased by entering Sick Pay hours in check entry.  """  
      self.SickHrsMax:int = obj["SickHrsMax"]
      """  Maximum number of sick hours that can be accrued.  """  
      self.Division:str = obj["Division"]
      """  The override G/L Division for  G/L transactions created by payroll.   This can be left blank or must be valid in the GLDiv master.  The system attempts to use this in the construction of a G/L account number.  The system replaces the division and department components of the account from the appropriate master file (PayType, PRDeduc,  PRTaxMas...) with the PrEmpDat.Division/GlDept if they are non blank. If this combination yields a valid GL account (found in GLAcct and Active = yes) then it is used, else the original account defined by the master is  used. Note: Hours that are transferred from job costing uses the Division/GlDept overrides defined in the JCDept master to override the account defined in the PayType master.  """  
      self.GLDept:str = obj["GLDept"]
      """  The G/L Department default for payments made in this department.  This can be blank or must be valid in the GLDept master.  This is similar to the PREmpDat.Division, see that fields description for info about how the system creates default G/L accounts.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.ShopEmployee:bool = obj["ShopEmployee"]
      """  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  """  
      self.OTDay:int = obj["OTDay"]
      """  Overtime Threshold Day  """  
      self.OTWeek:int = obj["OTWeek"]
      """  Overtime Threshold Week  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific employee. To be view-as EDITOR widget.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the payroll employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also PREmpMas.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay for W2.  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  Indicates a retirement plan for W2.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier for an external interface.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory to release it for another Sales Order, Job or Transfer Order during the process of picking and packing orders.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      """  Indicates if the record is linked from HCM  """  
      self.InActive:bool = obj["InActive"]
      """  Indicates if the Employee is inactive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageFile:str = obj["ImageFile"]
      """  Path of photo id  """  
      self.PerConName:str = obj["PerConName"]
      self.SupervisorName:str = obj["SupervisorName"]
      """  Supervisor Name  """  
      self.DspSocSecNum:str = obj["DspSocSecNum"]
      """  Unencrypted Social Security Number for input and display purposes.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DcdUserIDName:str = obj["DcdUserIDName"]
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.UserCompName:str = obj["UserCompName"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  encoded value which identifies the employee.  """  
      self.RateDate:str = obj["RateDate"]
      """  Date at which the current PayRate became effective.  """  
      self.PayRate:int = obj["PayRate"]
      """  Hourly Pay Rate that is used in calculating the pay check amount.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.Salary:int = obj["Salary"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Identifies the tax master (PRTaxMas) that this EmpTax record is related to.  """  
      self.PerExempt:int = obj["PerExempt"]
      """  Number of personal exemptions that this employee is claiming for this tax.  """  
      self.DepExempt:int = obj["DepExempt"]
      """  Number of dependent exemptions that this employee is claiming for this tax.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  The tax filing status the employee claims for this tax. Using the TaxTblID and FileStatus must be valid in the PRTaxDtl file.  Examples would be S - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.AddlWithholding:int = obj["AddlWithholding"]
      """  Additional withholding amount.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Annual tax credit amount.  Normally the annual tax credit is calculated by the system as the # of personal/dependent exemptions multiplied by the credit value defined in the tax table. This value is to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  """  
      self.FixedEX:int = obj["FixedEX"]
      """  Fixed annual exemption amount.  Normally the annual exemption amount is calculated by the system as the # of personal/dependent exemptions multiplied by the exemption value defined in the tax table.  The FixedEX field is used to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  """  
      self.Exempt:bool = obj["Exempt"]
      """  Indicates that this employee is exempt from this tax.  This is used when an employee needs to be reported for taxes but should not have an actual tax calculated.  This is different than not setting up this tax for the employee in the first place.  """  
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. Inactive = Yes prevents the tax from being taken.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      self.TaxDetailFileStatusDesc:str = obj["TaxDetailFileStatusDesc"]
      """  From PRTaxDtl.FileStatus  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.TaxMasterDescription:str = obj["TaxMasterDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddEmployeeResultsLinkCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class AddEmployeeResultsLinkCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildClassList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.classList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildFilingList_input:
   """ Required : 
   taxTblID
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      """  Tax Table ID code  """  
      pass

class BuildFilingList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.filingList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildTaxTblList_input:
   """ Required : 
   taxTblID
   empID
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      """  Current Tax Table ID, blank if new  """  
      self.empID:str = obj["empID"]
      """  Curreny Employee ID  """  
      pass

class BuildTaxTblList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.taxList:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalcSalaryRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class CalcSalaryRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFileStatus_input:
   """ Required : 
   ProposedFileStatus
   ds
   """  
   def __init__(self, obj):
      self.ProposedFileStatus:str = obj["ProposedFileStatus"]
      """  propsed value  """  
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class ChangeFileStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckJCDeptExists_input:
   """ Required : 
   jcDept
   """  
   def __init__(self, obj):
      self.jcDept:str = obj["jcDept"]
      """  Job department to validate.  """  
      pass

class CheckJCDeptExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckLaborExpCodeExists_input:
   """ Required : 
   labExpCode
   """  
   def __init__(self, obj):
      self.labExpCode:str = obj["labExpCode"]
      """  Labor expense code to validate.  """  
      pass

class CheckLaborExpCodeExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckLeavePREmpMas_input:
   """ Required : 
   empId
   """  
   def __init__(self, obj):
      self.empId:str = obj["empId"]
      """  The current employee's ID  """  
      pass

class CheckLeavePREmpMas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPRClassExisst_input:
   """ Required : 
   classID
   """  
   def __init__(self, obj):
      self.classID:str = obj["classID"]
      """  Class to validate.  """  
      pass

class CheckPRClassExisst_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPRWorkCompCodeExists_input:
   """ Required : 
   workCompCode
   """  
   def __init__(self, obj):
      self.workCompCode:str = obj["workCompCode"]
      """  Worker's compensation code to validate.  """  
      pass

class CheckPRWorkCompCodeExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPayRateEffectiveDate_input:
   """ Required : 
   PayRateDate
   PREmpID
   PRRateSysRowID
   """  
   def __init__(self, obj):
      self.PayRateDate:str = obj["PayRateDate"]
      """  the pay rate date  """  
      self.PREmpID:str = obj["PREmpID"]
      """  the payroll employee id  """  
      self.PRRateSysRowID:str = obj["PRRateSysRowID"]
      """  the PREmpRt SysRowID  """  
      pass

class CheckPayRateEffectiveDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.OutMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPersonContact_input:
   """ Required : 
   PerConID
   EmpID
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      """  The Person Contact ID  """  
      self.EmpID:str = obj["EmpID"]
      """  ID of the current Employee  """  
      pass

class CheckPersonContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.OutMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpDedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  encoded value which identifies the employee.  """  
      self.DeductionID:str = obj["DeductionID"]
      """  The ID of the related deduction master  """  
      self.DeductionNum:int = obj["DeductionNum"]
      """  DeductionNum uniquely identifies a PREmpDed record for an employee, for a specific DeductionID.  This enables an employee to have the same Deduction established more than once without having to set up a new deduction master.  For example, you may have a deduction for loan repayments and the employee may have multiple loans each with there own declining balances established.  This integer is assigned by the system automatically by finding the last related records number and adding one to it.  """  
      self.Period1:bool = obj["Period1"]
      """  Indicates that this deduction is taken during deduction period 1. Deduction periods (of which there are five) provide a method of controlling when the deduction is to be taken.  When payroll is run you are asked to enter a deduction period.  Only deductions that have that period marked will be taken. An exception to this rule would be if the CarryOverAmt <> 0 (see CarryOverAmt).  """  
      self.Period2:bool = obj["Period2"]
      """  Indicates that this deduction is taken during deduction period 2.  (Also see Period1).  """  
      self.Period3:bool = obj["Period3"]
      """  Indicates if this deduction is taken during deduction period 3.  (Also see Period1).  """  
      self.Period4:bool = obj["Period4"]
      """  Indicates if this deduction is taken during deduction period 4.  (Also see Period1).  """  
      self.Period5:bool = obj["Period5"]
      """  Indicates if this deduction is taken during deduction period 5.  (Also see Period1).  """  
      self.Rate:int = obj["Rate"]
      """  Deduction Rate.  This can represent either a fixed amount or a percent of gross wages (see RateQualifier).  """  
      self.RateQualifier:str = obj["RateQualifier"]
      """   The value of this field qualifies the value stored in the Rate field as either a fixed amount, percent of gross or percent of net pay. Defaulted from PRDeduct.RateQualifier.
Amt = Amount,  %Grs = Percent of gross, %Net = Percent of Net.
Note:  %Net is not allowed if the deduction is exempt from any taxes (records in PRDedXTx).  if %Net then this deduction is calculated after all other deductions and taxes, regardless of the deduction being tax exempt.  A deduction could be %Net and marked as tax exempt if the deduction was made tax exempt after it had already been marked as %Net.  """  
      self.DeclineOrigAmt:int = obj["DeclineOrigAmt"]
      """  This is the original amount of the declining deduction.  It is used primarily as a reference.  """  
      self.DeclineRemAmt:int = obj["DeclineRemAmt"]
      """  This is the remaining amount of the declining deduction.  """  
      self.CheckLimit:int = obj["CheckLimit"]
      """  This value sets a maximum check limit on the amount of this deduction.  """  
      self.MonthLimit:int = obj["MonthLimit"]
      """  This value sets a maximum monthly limit on the amount of this deduction.  The month is determined by using the check date.  """  
      self.YearlyLimit:int = obj["YearlyLimit"]
      """  This value sets a maximum yearly limit on the amount of this deduction.  The year is determined by using the check date.  """  
      self.CarryOverAmt:int = obj["CarryOverAmt"]
      """  Amount carried over from previous pay period.  The system will attempt to deduct this amount in the very next pay period regardless of the deduction cycle.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. Inactive = Yes prevents the deduction from being taken.  """  
      self.Reference:str = obj["Reference"]
      """  Employee specific information that can be used to further describe the reason for the deduction. For example; you may have a generic deduction called "Purchases", using the reference you could identify what the employee's purchase was. This field is printed on the check stub.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific deduction.  """  
      self.BankRoutingNum:str = obj["BankRoutingNum"]
      """  Employee's Bank Routing Number  """  
      self.BankAcctNum:str = obj["BankAcctNum"]
      """  Employee's Bank Account Number  """  
      self.BankAcctName:str = obj["BankAcctName"]
      """  The name the employee's bank account is under.  It doesn't have to match the employee's name.  """  
      self.BankAcctType:str = obj["BankAcctType"]
      """  The employee's bank account type:  C - Checking, S - Savings, etc.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      self.ElecDeposit:bool = obj["ElecDeposit"]
      self.CarryOver:bool = obj["CarryOver"]
      self.DeclineBalance:bool = obj["DeclineBalance"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.DeductionDescription:str = obj["DeductionDescription"]
      self.DeductionHCMLinked:bool = obj["DeductionHCMLinked"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.SocSecNum:str = obj["SocSecNum"]
      """  Encrypted Social security number.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.ClassID:str = obj["ClassID"]
      """   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  """  
      self.HireDate:str = obj["HireDate"]
      """  Date that employee was hired.  """  
      self.Terminated:bool = obj["Terminated"]
      """  Indicates if employee has been terminated.  """  
      self.TerminatedDate:str = obj["TerminatedDate"]
      """  Date that employee was terminated from employment.  """  
      self.PayType:str = obj["PayType"]
      """  H = Hourly,  S = Salaried.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  """  
      self.ShopEmployee:bool = obj["ShopEmployee"]
      """  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the payroll employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspSocSecNum:str = obj["DspSocSecNum"]
      """  Unencrypted Social Security Number for input and display purposes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpMasListTableset:
   def __init__(self, obj):
      self.PREmpMasList:list[Erp_Tablesets_PREmpMasListRow] = obj["PREmpMasList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PREmpMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value for employee which can be used to link the PREmpMas with it's sub related files.  This field is normally blank, which means file joins are impossible. This value can be set/reset only by the payroll manager via an option in system maintenance.  """  
      self.SocSecNum:str = obj["SocSecNum"]
      """  Encrypted Social security number.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.ClassID:str = obj["ClassID"]
      """   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.HireDate:str = obj["HireDate"]
      """  Date that employee was hired.  """  
      self.Terminated:bool = obj["Terminated"]
      """  Indicates if employee has been terminated.  """  
      self.TerminatedDate:str = obj["TerminatedDate"]
      """  Date that employee was terminated from employment.  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Employees birthday  """  
      self.PayType:str = obj["PayType"]
      """  H = Hourly,  S = Salaried.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  """  
      self.Pension:bool = obj["Pension"]
      """  Indicates if this employee is part of a pension plan.  This is used to print on the W2 form  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Indicates if this employee is part of a deferred compensation plan.  This is used to print on the W2 form  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The workman's compensation master that this employee is related to.  """  
      self.VacAccrualRate:int = obj["VacAccrualRate"]
      """  The number of hours of vacation time that is earned per pay period.  """  
      self.VacRemaining:int = obj["VacRemaining"]
      """  Vacation hours remaining. This field can be updated through master maintenance.  It is increased by the VacAccuralRate value for each period the employee is paid. It is reduced when vacation hours are entered in check entry.  """  
      self.VacHrsMax:int = obj["VacHrsMax"]
      """  Maximum number of vacation hours that can be accrued.  """  
      self.SickAccrualRate:int = obj["SickAccrualRate"]
      """  The number of hours of sick time that is earned per pay period.  """  
      self.SickRemaining:int = obj["SickRemaining"]
      """  Total Sick hours remaining.  This field can be directly maintained via employee master maintenance.  It gets increased by the SickAccrualRate value for each period an employee gets paid in.  It is decreased by entering Sick Pay hours in check entry.  """  
      self.SickHrsMax:int = obj["SickHrsMax"]
      """  Maximum number of sick hours that can be accrued.  """  
      self.Division:str = obj["Division"]
      """  The override G/L Division for  G/L transactions created by payroll.   This can be left blank or must be valid in the GLDiv master.  The system attempts to use this in the construction of a G/L account number.  The system replaces the division and department components of the account from the appropriate master file (PayType, PRDeduc,  PRTaxMas...) with the PrEmpDat.Division/GlDept if they are non blank. If this combination yields a valid GL account (found in GLAcct and Active = yes) then it is used, else the original account defined by the master is  used. Note: Hours that are transferred from job costing uses the Division/GlDept overrides defined in the JCDept master to override the account defined in the PayType master.  """  
      self.GLDept:str = obj["GLDept"]
      """  The G/L Department default for payments made in this department.  This can be blank or must be valid in the GLDept master.  This is similar to the PREmpDat.Division, see that fields description for info about how the system creates default G/L accounts.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.ShopEmployee:bool = obj["ShopEmployee"]
      """  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  """  
      self.OTDay:int = obj["OTDay"]
      """  Overtime Threshold Day  """  
      self.OTWeek:int = obj["OTWeek"]
      """  Overtime Threshold Week  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific employee. To be view-as EDITOR widget.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the payroll employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also PREmpMas.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay for W2.  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  Indicates a retirement plan for W2.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier for an external interface.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory to release it for another Sales Order, Job or Transfer Order during the process of picking and packing orders.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      """  Indicates if the record is linked from HCM  """  
      self.InActive:bool = obj["InActive"]
      """  Indicates if the Employee is inactive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageFile:str = obj["ImageFile"]
      """  Path of photo id  """  
      self.PerConName:str = obj["PerConName"]
      self.SupervisorName:str = obj["SupervisorName"]
      """  Supervisor Name  """  
      self.DspSocSecNum:str = obj["DspSocSecNum"]
      """  Unencrypted Social Security Number for input and display purposes.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DcdUserIDName:str = obj["DcdUserIDName"]
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.UserCompName:str = obj["UserCompName"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  encoded value which identifies the employee.  """  
      self.RateDate:str = obj["RateDate"]
      """  Date at which the current PayRate became effective.  """  
      self.PayRate:int = obj["PayRate"]
      """  Hourly Pay Rate that is used in calculating the pay check amount.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.Salary:int = obj["Salary"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmpTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Identifies the tax master (PRTaxMas) that this EmpTax record is related to.  """  
      self.PerExempt:int = obj["PerExempt"]
      """  Number of personal exemptions that this employee is claiming for this tax.  """  
      self.DepExempt:int = obj["DepExempt"]
      """  Number of dependent exemptions that this employee is claiming for this tax.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  The tax filing status the employee claims for this tax. Using the TaxTblID and FileStatus must be valid in the PRTaxDtl file.  Examples would be S - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.AddlWithholding:int = obj["AddlWithholding"]
      """  Additional withholding amount.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Annual tax credit amount.  Normally the annual tax credit is calculated by the system as the # of personal/dependent exemptions multiplied by the credit value defined in the tax table. This value is to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  """  
      self.FixedEX:int = obj["FixedEX"]
      """  Fixed annual exemption amount.  Normally the annual exemption amount is calculated by the system as the # of personal/dependent exemptions multiplied by the exemption value defined in the tax table.  The FixedEX field is used to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  """  
      self.Exempt:bool = obj["Exempt"]
      """  Indicates that this employee is exempt from this tax.  This is used when an employee needs to be reported for taxes but should not have an actual tax calculated.  This is different than not setting up this tax for the employee in the first place.  """  
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. Inactive = Yes prevents the tax from being taken.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpID:str = obj["EmpID"]
      self.TaxDetailFileStatusDesc:str = obj["TaxDetailFileStatusDesc"]
      """  From PRTaxDtl.FileStatus  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.TaxMasterDescription:str = obj["TaxMasterDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PREmployeeTableset:
   def __init__(self, obj):
      self.PREmpMas:list[Erp_Tablesets_PREmpMasRow] = obj["PREmpMas"]
      self.PREmpMasAttch:list[Erp_Tablesets_PREmpMasAttchRow] = obj["PREmpMasAttch"]
      self.PREmpDed:list[Erp_Tablesets_PREmpDedRow] = obj["PREmpDed"]
      self.PREmpRt:list[Erp_Tablesets_PREmpRtRow] = obj["PREmpRt"]
      self.PREmpTax:list[Erp_Tablesets_PREmpTaxRow] = obj["PREmpTax"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPREmployeeTableset:
   def __init__(self, obj):
      self.PREmpMas:list[Erp_Tablesets_PREmpMasRow] = obj["PREmpMas"]
      self.PREmpMasAttch:list[Erp_Tablesets_PREmpMasAttchRow] = obj["PREmpMasAttch"]
      self.PREmpDed:list[Erp_Tablesets_PREmpDedRow] = obj["PREmpDed"]
      self.PREmpRt:list[Erp_Tablesets_PREmpRtRow] = obj["PREmpRt"]
      self.PREmpTax:list[Erp_Tablesets_PREmpTaxRow] = obj["PREmpTax"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PREmployeeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PREmployeeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PREmployeeTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDeductDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class GetDeductDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetEmpIDInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class GetEmpIDInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetEmpLinkValue_input:
   """ Required : 
   inEmpID
   """  
   def __init__(self, obj):
      self.inEmpID:str = obj["inEmpID"]
      """  in Employee Link  """  
      pass

class GetEmpLinkValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outEmpLink:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_PREmpMasListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPREmpDed_input:
   """ Required : 
   ds
   empLink
   deductionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.empLink:str = obj["empLink"]
      self.deductionID:str = obj["deductionID"]
      pass

class GetNewPREmpDed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPREmpMasAttch_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewPREmpMasAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPREmpMas_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class GetNewPREmpMas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPREmpRt_input:
   """ Required : 
   ds
   empLink
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.empLink:str = obj["empLink"]
      pass

class GetNewPREmpRt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPREmpTax_input:
   """ Required : 
   ds
   empLink
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.empLink:str = obj["empLink"]
      pass

class GetNewPREmpTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartner_input:
   """ Required : 
   ds
   partnerNum
   partnerType
   partnerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.partnerNum:int = obj["partnerNum"]
      self.partnerType:int = obj["partnerType"]
      self.partnerID:str = obj["partnerID"]
      pass

class GetNewPartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShopEmployee_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      """  Shop Employee's ID  """  
      pass

class GetNewShopEmployee_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOverrideList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search statement to filter the PREmpMas table on  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size (required)  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolte Page size (required)  """  
      pass

class GetOverrideList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PREmpMasListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   PerConID
   ds
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePREmpMas
   whereClausePREmpMasAttch
   whereClausePREmpDed
   whereClausePREmpRt
   whereClausePREmpTax
   whereClauseEntityGLC
   whereClausePartner
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePREmpMas:str = obj["whereClausePREmpMas"]
      self.whereClausePREmpMasAttch:str = obj["whereClausePREmpMasAttch"]
      self.whereClausePREmpDed:str = obj["whereClausePREmpDed"]
      self.whereClausePREmpRt:str = obj["whereClausePREmpRt"]
      self.whereClausePREmpTax:str = obj["whereClausePREmpTax"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClausePartner:str = obj["whereClausePartner"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PREmployeeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetShopEmployeeInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class GetShopEmployeeInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
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

class ModifySearchIDs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class ModifySearchIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveEmployeeResultsLinkCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class RemoveEmployeeResultsLinkCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPREmployeeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPREmployeeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePayRate_input:
   """ Required : 
   empLink
   rateDate
   """  
   def __init__(self, obj):
      self.empLink:str = obj["empLink"]
      self.rateDate:str = obj["rateDate"]
      pass

class ValidatePayRate_output:
   def __init__(self, obj):
      pass

class ValidateRequiredFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

class ValidateRequiredFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PREmployeeTableset] = obj["ds"]
      pass

      """  output parameters  """  

